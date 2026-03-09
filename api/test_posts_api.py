import pytest
from jsonschema import validate
from api.api_client import get_posts, get_endpoint


# schema validation
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}


def test_response_time():
    response = get_posts()
    assert response.elapsed.total_seconds() < 2

def test_schema_validation():
    response = get_posts()
    posts = response.json()
    for post in posts:
        validate(instance=post, schema=post_schema)

# parametrization of endpoints
@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/users"
])
def test_multiple_endpoints(endpoint):
    response = get_endpoint(endpoint)
    assert response.status_code == 200