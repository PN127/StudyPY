
from schemas import User

users: list[User] = [
    User(
        id = 1,
        name = 'Bob',
        age = 10,
        email = 'bob@gmail.com' 
    ),
    User(
        id = 2,
        name = 'Alex',
        age = 15,
        email = 'alex@gmail.com' 
    ),
]