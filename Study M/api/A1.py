import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())


new_post = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(response.json())


