import os
import sys
from elasticsearch import AsyncElasticsearch
from models.check import IndividualAttributes, MatchingRule
from models.store import SingleIndividualAttributes, BulkIndividualAttributes
from services.elastic_search import ElasticSearchClient # noqa
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HOST = os.getenv("ELASTIC_HOST")
PORT = os.getenv("ELASTIC_PORT")
INDEX_NAME = os.getenv("ELASTIC_INDEX_NAME")

hosts = f"http://{HOST}:{PORT}"

# Connect to Elastic Search
session = AsyncElasticsearch(hosts=hosts)

# Declare the ES client
client = ElasticSearchClient(session=session)


# Dependencies
async def search_user_in_es(attributes: IndividualAttributes):
    return await client.get_top_search_names_and_probabilities(INDEX_NAME, attributes.dict()) # noqa


async def update_single_entry(attributes: SingleIndividualAttributes):
    return await client.update_single_entry(INDEX_NAME, attributes.dict())


async def update_bulk_entries(attributes: BulkIndividualAttributes):
    return await client.update_bulk_entries(INDEX_NAME, attributes.dict())


async def update_matching_rule(matching_rule: MatchingRule):
    # Read current rule from config json file
    print(matching_rule)

    # Update config rule

    # Save JSON
    
    return None
