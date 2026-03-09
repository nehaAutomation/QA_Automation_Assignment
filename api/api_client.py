import requests
from utils.config import BASE_API_URL

def get_endpoint(endpoint):
    return requests.get(f"{BASE_API_URL}{endpoint}")

def get_posts():
    response = requests.get(f"{BASE_API_URL}/posts")
    return response

