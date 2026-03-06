import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print(response)

if response.status_code ==200:
    print("status code is 200, hence request is successful")
else:
    print("unsuccessful request")

#converting response to JSON
posts = response.json()

req_keys = {"userId", "id", "title", "body"}


for i in posts:
    assert req_keys.issubset(i.keys()), "missing keys in response"

first_five_posts = posts[:5]

with open("first_five_posts.json", "w") as file:
    json.dump(first_five_posts, file, indent=4)

print("first 5 posts saved successfully!!!")

if __name__ == "__main__":
    print("API Automation script is running")


