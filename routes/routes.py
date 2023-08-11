from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from models.models import Todo
from config.database import collection_name
from schema.schemas import list_serial, dict_serial, delete_request
from bson import ObjectId

router = APIRouter()

@router.get("/todos", status_code=status.HTTP_200_OK)
def get_todos():
    return list_serial(collection_name.find())
    
@router.post("/todos", status_code=status.HTTP_201_CREATED)
def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))
    return list_serial(collection_name.find())

@router.get("/todos/{id}")
def get_todo(id: str):
    return dict_serial(collection_name.find_one({"_id": ObjectId(id)}))

@router.put("/todos/{id}")
def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": jsonable_encoder(todo, exclude_unset=True)})

@router.delete("/todos/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: str):
    return delete_request(id)
    
    
    
     
