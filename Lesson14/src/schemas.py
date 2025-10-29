from pydantic import BaseModel, Field

class BaseUser(BaseModel):
    name: str
    age: int
    bio: str
    password: str

class CreateUser(BaseUser):
    ...

class UpdateUser(BaseModel):
    name: str | None = Field(None, max_length= 16)
    age: int | None = Field(None, ge=0, le=120)
    bio: str | None = Field(None)
    password: str | None = Field(None)

class User(BaseUser):
    id: int