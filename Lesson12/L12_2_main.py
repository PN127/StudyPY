from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()
@app.get('/')
def home() -> dict:
    return {'date': 'message'}  

@app.get('/contacts')
def contacts() -> int:
    return 34

posts= [
    {'id':1, 'title':'News1', 'body': 'Text1'},
    {'id':3, 'title':'News3', 'body': 'Text3'},
    {'id':2, 'title':'News2', 'body': 'Text2'}
]

@app.get('/items')
def items() -> list:
    return posts
@app.get('/items/{id}')
def item(id: int):
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')

@app.get('/search')
def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
                if post['id'] == post_id:
                    return post
        raise HTTPException(status_code=404, detail='Post not found')

    else:
        return{'data':'No post id provided'}