import requests

url_users = "https://jsonplaceholder.typicode.com/posts?userId=1"
response = requests.get(url_users)

print("Статус:", response.status_code)
for i in response.json():
    print(i['title'])

url_comments = 'https://jsonplaceholder.typicode.com/comments'
comment = {
    'postId': 1,
    'name' : 'имя',
    'email':'stud',
    'comment' : 'это комментарий к первому или второму посту'
}
response2 = requests.post(url_comments, json=comment)
print("Статус:", response2.status_code)
print('Answer', response2.json())
