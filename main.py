from fastapi import FastAPI

app = FastAPI()

users = [
    {
        'id': 1,
        'name': 'Sumeet'
    },
    {
        'id': 2,
        'name': 'Sumeet2'
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

@app.get("/")
async def root():
    return {"message": "Hello world"}