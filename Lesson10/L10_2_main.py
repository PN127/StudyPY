import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print("Статус:", response.status_code)
print("Первый пост:", response.json()[0])
print('Title: ', response.json()[0]['title'])
print('Body: ', response.json()[0]['body'])