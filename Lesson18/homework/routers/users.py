from fastapi import APIRouter, Depends, Request
from services.user_service import *
from services.auth_service import get_current_user
from schemas import *

router = APIRouter()

# @router.post('')
# def post_user(schema: BaseUser) -> User:
#     user = create_user(schema)
#     return user

@router.get('/me')
def read_current_user(request: Request, current_user = Depends(get_current_user)):
    
    return {'email': current_user.email, 'name': current_user.name} 

@router.get('')
def get_users()->list[User]:
    users = read_users()
    return users

@router.get('/{id}')
def get_user(id: int) -> User:
    user = read_user(id)
    return user

@router.put('/{id}')
def put_user(id: int, schema: UpdateUser) -> User:
    return update_user(id, schema)

@router.delete('/{id}')
def delete_user(id: int) -> bool:
    return delete_user_1(id)

