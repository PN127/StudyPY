from fastapi import HTTPException, Response, Request

from schemas import *
from services.user_service import *

from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta, timezone
from jose import jwt
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine, UserDB

def register_user(schema: BaseUser) -> User:
    with Session(engine) as session:
        hash_password = pbkdf2_sha256.hash(schema.password)
        new_user = UserDB(**schema.model_dump(exclude={"password"}),
                          password=hash_password) #исключаем password из model_dump и присваиваем новое значение password
        session.add(new_user)
        session.commit()
        user = User(**new_user.to_dict())
    return user

def login_user(schema: LoginUser, response: Response) -> str:
    user = find_user(schema.email)
    if not pbkdf2_sha256.verify(schema.password, user.password):
        raise HTTPException(401, 'Password is not correct')
    token = create_access_token({'sub': schema.email})
    response.set_cookie('my_access_token', token)
    return {"access_token": token, "token_type": "Bearer"}


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def get_current_user(request: Request):
    try:
        token = request.cookies.get('my_access_token')
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        email:str = payload.get('sub')
        if email is None:
            raise HTTPException (401, 'Invalid token')
    except:
        raise HTTPException (401, 'Token decode error')
    userDB = find_user(email)
    user = User(**userDB.to_dict())
    return user