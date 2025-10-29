from typing import Optional
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)#primary_key=True - Делает колонку первичным ключом с автоувеличением
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String(30))
    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r}, age={self.age!r}, email={self.email!r})'
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }


engine = create_engine('sqlite:///users_app.db', echo=True)
Base.metadata.create_all(engine)