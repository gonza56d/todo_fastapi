"""Project configurations."""

from typing import List

from fastapi import FastAPI, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor import motor_asyncio

from .models.todos import Todo, UpdateTodo


# FastAPI instance
app = FastAPI()

# MongoDB Connection
client = motor_asyncio.AsyncIOMotorClient('mongodb://root:example@mongo:27017/')
db = client.college


@app.get('/', response_description='List all the to-dos', response_model=List[Todo])
async def list_todos():
    todos = await db['todos'].find().to_list(500)
    return todos


@app.post('/', response_description='Add new to-do', response_model=Todo)
async def create_todo(todo: Todo = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = await db['todos'].insert_one(todo)
    created_todo = await db['todos'].find_one({'_id': new_todo.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_todo)


@app.get('/{id}', response_description='Get a signle to-do', response_model=Todo)
async def show_todo(id: str):
    if (todo := await db["todos"].find_one({"_id": id})) is not None:
        return todo
    raise HTTPException(status_code=404, detail=f'Todo {id} not found')


@app.put('/{id}', response_description='Update a to-do', response_model=Todo)
async def update_todo(id: str, todo: UpdateTodo = Body(...)):
    todo = {k: v for k, v in todo.dict().items() if v is not None}

    if len(todo) >= 1:
        update_result = await db['todos'].update_one({'_id': id}, {'$set': todo})

        if update_result.modified_count == 1:
            if (updated_todo := await db['todos'].find_one({'_id': id})) is not None:
                return updated_todo

    if (existent_todo := await db['todos'].find_one({'_id': id})) is not None:
        return existent_todo
    
    raise HTTPException(status_code=404, detail=f'To-do {id} not found')


@app.delete('/{id}', response_description='Delete a to-do')
async def delete_todo(id: str):
    delete_result = await db['todos'].delete_one({'_id': id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f'To-do {id} not found')
