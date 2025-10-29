from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

users: List[User] = []


@app.post('/register')
def register(user: Annotated[
    User, Body(
        ...,
        title='Регистрация пользователя',
        example={
            'name':'UserName',
            'age':1,
            'email':'p@ya.ru'
        })]):
    
    users.append(user)
    response = {
        'message':f'Пользователь {user.name} успешно зарегистрирован с возрастом {user.age} и почтой {user.email}',
        'user':user        
        }
    return response