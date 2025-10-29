from fastapi import HTTPException
from schemas import *
from data import users


def create_user(schema: BaseUser) -> User:
    new_user_id = len(users) + 1
    new_user = User(**schema.model_dump(), id= new_user_id)
    users.append(new_user)

    return new_user

def read_users()->list[User]:
    return users

def read_user(id: int) -> User:
    user = next((user for user in users if user.id == id), None)
    if not user:
        raise HTTPException(404, 'User not found')
    return user

def update_user(id: int, schema: UpdateUser):
    user = read_user(id)
    user_index = users.index(user)
    updated_user = User(**schema.model_dump(), id=id)

    users[user_index] = updated_user

def delete_user_1(id: int) -> bool:
    user = read_user(id)
    users.remove(user)
    return True