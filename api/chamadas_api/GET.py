import requests

url = "https://jsonplaceholder.typicode.com/posts/1"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print("Título do post: ", data['title'])
    print("Corpo do post: ", data['body'])
else:
    print("Erro", response.status_code)