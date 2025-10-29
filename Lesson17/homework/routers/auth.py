from fastapi import APIRouter
from services.auth_service import *
from services.user_service import find_user
from schemas import *


router = APIRouter()

@router.post('/register')
def register(schema: RegisterUser) -> User:
    return register_user(schema)

@router.post('/login')
def login(schema: LoginUser):
    return login_user(schema)
