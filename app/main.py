"""Project configurations."""

# Python
from typing import Optional
# FastAPI
from fastapi import FastAPI


# FastAPI instance
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello world'}
