from fastapi import FastAPI

from schemas import *
from data import users
from deps import UserDepends

app = FastAPI()


@app.post('/users')
async def create_user(schema: CreateUser)->User:
    new_user_id = len(users) + 1
    # model_dump() возвращает dict (pydantic v2). Вызываем функцию.
    user = User(**schema.model_dump(), id=new_user_id)
    users.append(user)

    return user

@app.get('/users')
async def get_users()->list[User]:
    return users


@app.get('/users/{id}')
async def get_user(user: UserDepends) -> User:
    return user

@app.put('/users/{id}')
async def update_user(user: UserDepends, schema: UpdateUser) ->User:
    updated_data = schema.model_dump(exclude_unset=True)
    updated_user = user.model_copy(update=updated_data)

    user_index = users.index(user)
    users[user_index] = updated_user

    return updated_user

@app.delete('/users/{id}')
async def delete_user(user: UserDepends) -> bool:
    users.remove(user)
    return True