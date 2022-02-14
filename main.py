from fastapi import FastAPI
from enum import Enum


app = FastAPI()

users = [
    {
        'id': 1,
        'name': 'Sumeet',
        'type': 'admin'
    },
    {
        'id': 2,
        'name': 'Sumeet2',
        'type': 'normal'
    }
]

notes = [
    {
        'user': 1,
        'todo': 'To go shopping.'
    },
    {
        'user': 2,
        'todo': 'To go library.'
    },
    {
        'user': 1,
        'todo': 'Complete the project.'
    }
]

class UserType(str, Enum):
    normal = 'normal'
    admin = 'admin'

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    
    for v in users:
        print(v['id'])
        if v['id'] == user_id:
            return v
