from typing import Annotated
from fastapi import HTTPException, Depends
from schemas import User
from data import users


def check_user(id: int) -> User:
    user = next((user for user in users if user.id == id), None)
    if not user:
        raise HTTPException(404, 'User not found')
    return user

UserDepends = Annotated[User, Depends(check_user)]