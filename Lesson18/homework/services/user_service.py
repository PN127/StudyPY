from fastapi import HTTPException
from schemas import *

from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine, UserDB


def read_users()->list[User]:
    with Session(engine) as session:
        slct = select(UserDB)
        users_DB = session.scalars(slct).fetchall()
        users: list[User] = []
        for user in users_DB:
            u = User(**user.to_dict())
            users.append(u)
    
    return users
    

def read_user(id: int) -> User:
    with Session(engine) as session:
        user_DB = session.get(UserDB, id)
        if not user_DB:
            raise HTTPException(404, 'User not foud')
        
        user = User(**user_DB.to_dict())
    return user

def find_user(email: str) -> UserDB:
    with Session(engine) as session:
        stmt = select(UserDB).where(UserDB.email == email)
        user = session.scalars(stmt).first()
        if not user:
            raise HTTPException(404, 'User not foud')
    return user

def update_user(id: int, schema: UpdateUser) -> User:
    with Session(engine) as session:
        user_DB = session.get(UserDB, id)
        if not user_DB:
            raise HTTPException(404, 'User not foud')
        
        updated_data = schema.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(user_DB, field, value)
            # setattr(object, name, value) - встроенная функция в Python, которая
            # устанавливает значение атрибута объекта динамически во время выполнения. Это
            # полезно, когда имя атрибута и/или значение заранее неизвестно и
            # содержится в переменной

            # Аргументы:
            # object — объект, атрибут которого нужно изменить.
            # name — имя атрибута (строка). Можно указывать как имя нового, 
            #        так и существующего атрибута.
            # value — значение, которое нужно присвоить атрибуту.

        user = User(**user_DB.to_dict())
        session.commit()

                   
    return user

def delete_user_1(id: int) -> bool:
    with Session(engine) as session:
        user_DB = session.get(UserDB, id)
        if not user_DB:
            raise HTTPException(404, 'User not foud')
        session.delete(user_DB)
        session.commit()
    
    return True