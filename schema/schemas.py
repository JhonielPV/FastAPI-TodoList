from fastapi import HTTPException, status
from config.database import collection_name
from bson import ObjectId

def serializer(todo: dict):
    return {
        "id": str(todo['_id']),
        "name": todo['name'],
        "description": todo['description'],
        "complete": todo['complete'],
    }

def list_serial(todos: list):
    return [serializer(todo) for todo in todos]

def dict_serial(todos: dict):
    if todos:
        todos['_id'] = str(todos['_id'])
        return [todos]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {todos['_id']} not found")

def delete_request(id: str):
    todo_id = collection_name.find_one({"_id": ObjectId(id)})
    
    if not todo_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {id} not found")
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

    return {"message": "Deleted Successfully"}
    
    
    

    
