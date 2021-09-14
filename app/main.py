"""Project configurations."""

from fastapi import FastAPI
from motor import motor_asyncio


# FastAPI instance
app = FastAPI()

# MongoDB Connection
client = motor_asyncio.AsyncIOMotorClient('mongodb://root:example@mongo:27017/')
db = client.college


@app.get('/')
async def root():
    return {'message': 'hello world'}
