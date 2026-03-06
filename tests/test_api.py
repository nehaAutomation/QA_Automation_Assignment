import requests
import pytest
from jsonschema import validate


URL = "https://jsonplaceholder.typicode.com"

#schema validation
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type":"number"},
        "id":{"type":"number"},
        "title":{"type":"string"},
        "body":{"type":"string"}
    },
    "required": ["userId", "id", "title", "body"]
}

def test_response_time():
    response= requests.get(f"{URL}/posts")
    assert response.elapsed.total_seconds()< 2

def test_schema_validation():
    response = requests.get(f"{URL}/posts")
    posts= response.json()

    for i in posts:
        validate(instance=i, schema=post_schema)

#parametrization of endpoints
@pytest.mark.parametrize("endpoint",[
    "/posts",
    "/comments",
    "/users"
])
def test_multiple_endpoints(endpoint):
    response= requests.get(f"{URL}{endpoint}")
    assert response.status_code==200