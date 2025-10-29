from fastapi import APIRouter
from services.user_service import *
from schemas import *

router = APIRouter()

@router.post('/user')
def post_user(schema: BaseUser) -> User:
    user = create_user(schema)
    return user

@router.get('/user')
def get_users()->list[User]:
    users = read_users()
    return users


@router.get('/user/{id}')
def get_user(id: int) -> User:
    user = read_user(id)
    return user

@router.put('/user/{id}')
def put_user(id: int, schema: UpdateUser) -> User:
    return update_user(id, schema)

@router.delete('/user/{id}')
def delete_user(id: int) -> bool:
    return delete_user_1(id)

