import os
import sys
import asyncio
from elasticsearch import AsyncElasticsearch
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))
from services.elastic_search import ElasticSearchClient # noqa

# Load environment variables
load_dotenv()
HOST = os.getenv("ELASTIC_HOST")
PORT = os.getenv("ELASTIC_PORT")
TEST_INDEX_NAME = os.getenv("TEST_INDEX_NAME")

hosts = f"http://{HOST}:{PORT}"

# Connect to Elastic Search
con = AsyncElasticsearch(hosts=hosts)
es_client = ElasticSearchClient(con)


async def test_search_index():
    payload = {
                "firstname": "James",
                "last_name": "Jones"
            }
    result = await es_client.search_identity(TEST_INDEX_NAME, payload)
    print(result)
    return result


async def test_elastic_search():
    await test_search_index()

    # Close connection
    await con.transport.close()

asyncio.run(test_elastic_search())
