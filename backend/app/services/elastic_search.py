from elasticsearch import AsyncElasticsearch, helpers
from typing import Union, Dict, List
from models.check import MatchedEntity, MatchedEntities


class ElasticSearchClient:
    '''
        Elastic Search python client. This will be used to query documents to 
        find the most appropriate match.

        Thin wrapper around the Elasticsearch package
    '''
    def __init__(self, session: AsyncElasticsearch):
        self.session = session

    async def search_identity(self, index: str, input_json: dict) -> Union[List, List[Dict]]: # noqa
        '''
        Search query in index. eg search for first_name, last_name in the
        identifiction index

        Parameters
        ----------
        index_name: str - Name of the index to be searched
        input_json: dict - JSON from front end containing info to be queried

        Returns
        ---------
        result: Union[List, List[Dict}] - list containing results of the search
                        ie list of hits based on the query
        '''
        # Convert input to query
        query = await self.get_es_query(input_json)

        # Get rescore query
        rescore_query = await self.get_rescore_query(input_json)

        # Build ES query from input_query. Use default ES caching
        response = await self.session.search(index=index,
                                             query=query,
                                             rescore=rescore_query,
                                             request_cache=True)

        # Get all hits
        hits = response["hits"]["hits"]

        return hits

    async def get_top_search_names_and_probabilities(self, index: str, input_json: dict) -> Union[MatchedEntities, MatchedEntity]: # noqa
        '''
        Wrapper on search_identity to get a pydantic model output

        Parameters
        ----------
        index_name: str - Name of the index to be searched
        input_json: dict - JSON from front end with info to be queried

        Returns
        ---------
        result: Union[MatchedEntities, MatchedEntity] - models containing
            first_name, last_name and score(probability) of top hits
        '''
        # Search for identities from elastic search
        hits = await self.search_identity(index, input_json)

        # Output list from list
        max_score = hits[0]["_score"]

        # Parse matches to model
        result_list = []
        for hit in hits:
            if hit["_score"] == max_score:
                model_dict = {"first_name": hit["_source"]["first_name"],
                              "last_name": hit["_source"]["last_name"],
                              "probability": hit["_score"]}

                # Parse dict to models
                model = MatchedEntity.parse_obj(model_dict)
                result_list.append(model)

        result = result_list if len(result_list) > 1 else result_list[0]

        return result

    async def get_es_query(self, input_json: dict) -> Dict:
        '''
            Convert the input json to an actual query based on configurations

            Parameters
            --------------
            input_json (dict): Should contain first and last name, birthdate
                                and identification (input from frontend in
                                dict form)

            Returns
            ---------------
            query (dict): Dict containing query information to be used by
                            search client
        '''
        # Capitalise first and last name
        last_name = input_json["last_name"].capitalize()
        first_name = input_json["first_name"].capitalize()

        # Keep only number values
        identification = input_json["identification"]
        birthdate = input_json["birthdate"]

        query = {
                "bool": {
                    "must": {
                        "match": {
                            "last_name": last_name
                        }
                    },
                    "should": [
                        {
                            "match": {
                                "birthdate": birthdate
                            }
                        },
                        {
                            "match": {
                                "identification": identification
                            }
                        }
                    ],
                    "filter": {
                        "regexp": {
                            "first_name.keyword": {
                                "value": f"{first_name[0]}.*",
                                "flags": "ALL"
                                }
                            }
                    },
                    "boost": 0
                }
            }

        return query

    async def get_rescore_query(self, input_json: Dict) -> Dict:
        '''
            Convert the input json to rescore query based on configurations.
            Defines the _score to be attributed to each hit

            Parameters
            --------------
            input_json (dict): Should contain first and last name, birthdate
                                and identification (input from frontend in
                                dict form)

            Returns
            ---------------
            rescore_query (dict): Dict containing rescore query information to
                                    be used by search client
        '''
        # Capitalise first and last name
        last_name = input_json["last_name"].capitalize()
        first_name = input_json["first_name"].capitalize()

        # Keep only number values
        identification = input_json["identification"]
        birthdate = input_json["birthdate"]

        # Define all queries
        rescore_query = [
                            {"query": {
                                "rescore_query": {
                                    "script_score": {
                                        "script": {
                                            "source": "0.4"
                                        },
                                        "query": {
                                            "match": {
                                                "last_name": last_name
                                            }
                                        }
                                    }
                                },
                                "score_mode": "total",
                                "query_weight": 0.4,
                                "rescore_query_weight": 1
                            }},
                            {"query": {
                                "rescore_query": {
                                    "script_score": {
                                        "script": {
                                            "source": "1"
                                        },
                                        "query": {
                                                "match": {
                                                    "identification": identification # noqa
                                                }
                                            }
                                    }
                                },
                                "score_mode": "max",
                                "query_weight": 1,
                                "rescore_query_weight": 1
                            }},
                            {"query": {
                                "rescore_query": {
                                    "script_score": {
                                        "script": {
                                            "source": "1"
                                            },
                                        "query": {
                                            "match": {
                                                "birthdate": birthdate
                                            }
                                        }
                                    }
                                },
                                "score_mode": "max",
                                "query_weight": 1,
                                "rescore_query_weight": 1
                            }},
                            {"query": {
                                "rescore_query": {
                                    "script_score": {
                                        "script": {
                                            "source": "0.2"
                                        },
                                        "query": {
                                            "match": {
                                                "first_name": first_name
                                            }
                                        }
                                    }
                                },
                                "score_mode": "total",
                                "query_weight": 0.4,
                                "rescore_query_weight": 1
                            }},
                        ]

        return rescore_query

    async def update_single_entry(self, index: str, input_json: Dict):
        '''
            Update a document in an index.

            Parameters
            ---------------
            input_json (dict): Should contain first and last name, birthdate
                                and identification (input from frontend in
                                dict form)
            index (str): Name of the index to update

            Returns
            ---------------
            result (dict): result dictionary
        '''
        return await self.session.index(index=index, body=input_json)

    async def update_bulk_entries(self, bulk_input_json: List[Dict]):
        '''
            Update multiple documents in an index.

            Parameters
            ---------------
            input_json_bulk (dict): Should contain first and last name
                                birthdate and identification (input from
                                frontend in dict form)

            index (str): Name of the index to update

            Returns
            ---------------
            message (dict): Success message
        '''
        # Bulk upload
        helpers.bulk(self.session, bulk_input_json)
        return {"Message": "Success"}
