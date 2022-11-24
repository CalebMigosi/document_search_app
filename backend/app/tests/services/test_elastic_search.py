import os
import sys
import asyncio
import time
import pytest
from typing import List
from elasticsearch import AsyncElasticsearch
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))
from services.elastic_search import ElasticSearchClient # noqa
from models.check import MatchedEntities, MatchedEntity

# Load environment variables
load_dotenv()
HOST = os.getenv("TEST_ELASTIC_HOST")
PORT = os.getenv("TEST_ELASTIC_PORT")
TEST_INDEX_NAME = os.getenv("TEST_INDEX_NAME")

hosts = f"http://{HOST}:{PORT}"


@pytest.mark.asyncio
async def test_search_index_wrong_birthday():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "James",
                "last_name": "Jones",
                "identification": "000000000",
                "birthdate": "2000-01-01"
            }
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa

    assert result == []

    # Close connection
    await con.transport.close()

    return result


@pytest.mark.asyncio
async def test_search_index_wrong_lastname():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "James",
                "last_name": "Jon",
                "identification": "000000000",
                "birthdate": "2000-01-01"
            }
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa

    assert result == []

    # Close connection
    await con.transport.close()

    return result


@pytest.mark.asyncio
async def test_search_index_correct_lastname():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "J.",
                "last_name": "Jones",
                "identification": "MISSING",
                "birthdate": "0000-01-01"
            }
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa

    # Should have 1 entry created in create_db.sh
    assert (type(result) == MatchedEntity) or (type(result) == MatchedEntities)
    if (type(result) == MatchedEntity):
        assert result.probability == "0.55"

    # Close connection
    await con.transport.close()

    return result


@pytest.mark.asyncio
async def test_search_index_correct_firstname():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "James",
                "last_name": "Jones",
                "identification": "MISSING",
                "birthdate": "0000-01-01"
            }
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa

    # Should have 1 entry created in create_db.sh
    assert (type(result) == MatchedEntity) or (type(result) == MatchedEntities)
    if (type(result) == MatchedEntity):
        assert result.probability == "0.6"

    # Close connection
    await con.transport.close()

    return result


@pytest.mark.asyncio
async def test_search_index_correct_id():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "James",
                "last_name": "Jones",
                "identification": "0",
                "birthdate": "0000-01-01"
            }
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa

    # Should have 1 entry created in create_db.sh
    assert (type(result) == MatchedEntity) or (type(result) == MatchedEntities)
    if (type(result) == MatchedEntity):
        assert result.probability == "1.0"

    # Close connection
    await con.transport.close()

    return result


@pytest.mark.asyncio
async def test_search_index():
    await test_search_index_wrong_birthday()
    await test_search_index_wrong_lastname()
    await test_search_index_correct_lastname()
    await test_search_index_correct_firstname()
    await test_search_index_correct_id()


@pytest.mark.asyncio
async def single_upload():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "TestFirtstName",
                "last_name": "TestLastName",
                "identification": "0000",
                "birthdate": "2000-01-01"
            }

    # Update single entry
    await es_client.update_single_entry(TEST_INDEX_NAME,
                                        input_json=input_json)

    # Close connection
    await con.transport.close()


@pytest.mark.asyncio
async def test_single_upload():
    # Connect to Elastic Search
    con = AsyncElasticsearch(hosts=hosts)
    es_client = ElasticSearchClient(con)

    input_json = {
                "first_name": "TestFirtstName",
                "last_name": "TestLastName",
                "identification": "0000",
                "birthdate": "2000-01-01"
            }
 
    # Search for item
    result = await es_client.get_top_search_names_and_probabilities(TEST_INDEX_NAME, input_json) # noqa
    assert (type(result) == MatchedEntity) or (type(result[0]) == MatchedEntity) # noqa

    if (type(result) == MatchedEntity):
        assert result.probability == "1.0"

    await con.transport.close()


@pytest.mark.asyncio
async def test_elastic_search():
    await test_search_index()
    await single_upload()
    time.sleep(5)
    await test_single_upload()

asyncio.run(test_elastic_search())
