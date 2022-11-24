from fastapi.testclient import TestClient
import sys
import os
from dotenv import load_dotenv
SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))
from main import create_app

load_dotenv()
APM_URL = os.getenv("TEST_ELASTIC_APM_SERVER_URL")

app = create_app(apm_url=APM_URL)
client = TestClient(app)


def test_get_client():
    input_json = {
                    "first_name": "James",
                    "last_name": "Jones"
                }
    response = client.post("/check",
                           json=input_json)
    assert response.status_code == 200


def test_upload_document():
    input_json = {
                "first_name": "TestFirstName",
                "last_name": "TestLastName",
                "identification": "0000",
                "birthdate": "2000-01-01"
            }
    response = client.post("/store",
                           json=input_json)
    assert response.status_code == 200


def test_bulk_upload_document():
    input_json = {"entries": [{
                "first_name": "TestThirdName",
                "last_name": "TestThirdName",
                "identification": "0000",
                "birthdate": "2000-01-01"
            },
            {
                "first_name": "TestSecondName",
                "last_name": "TestSecondName",
                "identification": "0001",
                "birthdate": "2000-01-01"
            }]}
    response = client.post("/store_bulk",
                           json=input_json)
    assert response.status_code == 200
