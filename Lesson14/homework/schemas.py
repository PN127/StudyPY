from pydantic import BaseModel, Field

class BaseUser(BaseModel):
    name: str
    age: int
    email: str

class UpdateUser(BaseModel):
    name: str | None = Field(None, max_length=20, min_length=2)
    age: int | None = Field(None, ge=0, le=120)
    email: str | None = Field(None)

class User(BaseUser):
    id: int
    
