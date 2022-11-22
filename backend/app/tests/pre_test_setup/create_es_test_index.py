from dotenv import load_dotenv
from elasticsearch import Elasticsearch, helpers
from itertools import product
from numpy import random
from datetime import datetime, timedelta
import os

# Load environment variables from env
load_dotenv()

# Connect to Elastic Search
session = Elasticsearch(hosts="http://localhost:9200")

INDEX_NAME = os.getenv("TEST_INDEX_NAME")


def create_test_database():
    '''
        Create test database. Central database used in all tests.
    '''
    # Create test index
    session.indices.create(index=INDEX_NAME)

    # Create random data for index
    first_names = ["James", "Kirua", "Chendi", "Abhishek", "Vladimir", ]
    last_names = ["Jones", "Jiang", "Patel", "Singh", "Mwangi"]

    names = [name for name in product(first_names, last_names)]
    ids = random.randint(100000000, 999999999, size=(len(names)))
    dates = [datetime.today() - timedelta(days=random.randint(5000, 10000))
             for i in range(len(ids))]

    # Create bulk data
    bulk_data = []
    for i, name in enumerate(names):
        data = {
            "first_name": name[0],
            "last_name": name[1],
            "birthdate": dates[i].strftime("%Y-%m-%d"),
            "identification": str(ids[i])
        }

        action = {
            "_index": INDEX_NAME,
            "_id": i,
            "_source": data
        }
        bulk_data.append(action)

    # Bulk upload
    helpers.bulk(session, bulk_data)

    # Refresh index
    session.indices.refresh(index=INDEX_NAME)

    resp = session.search(
        index=INDEX_NAME,
        query={"match_all": {}},
        size=20,
    )
    print(resp)


create_test_database()
