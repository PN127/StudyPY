from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()
items =[
    {'item':'a', 'price':1},
    {'item':'b', 'price':2},
    {'item':'c', 'price':3},
    {'item':'d', 'price':4},
    {'item':'e', 'price':5},
    {'item':'f', 'price':6},
    {'item':'g', 'price':7},
    {'item':'h', 'price':8},
    {'item':'k', 'price':9},
    {'item':'l', 'price':10},
    {'item':'m', 'price':11},
]

@app.get('/')
def home():
    return JSONResponse({'messgae':'Hello, FatsAPI!'}, status_code=200)

@app.get('/user/{name}')
def users(name: str) -> str:
    return JSONResponse({'user name': name}, status_code=200)

@app.get('/items')
def get_items(limit: int=Query(10, ge=0)):
    return items[:limit]
