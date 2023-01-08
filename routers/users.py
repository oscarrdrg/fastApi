from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/users", tags=["/users"], responses={404: {"message":"No encontrado"}})

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Oscar", surname="Rodrigo", age=23), User(id=2, name="Alvaro", surname="Majoral", age=23)]

@router.get("/")
async def users():
    return users_list


@router.get("/{id}")
async def users(id: int):
    return search_user(id)
   

@router.post("/")
async def user(user: User):

        if type(search_user(user.id)) == User:
            return {"error":"El usuario ya existe"}
        users_list.append(user)
        return {"message":"Se ha guardo el usuario correctamente",
                "user":user}

@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"Usuario no actualizado"}
    return user
    

@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
         return {"error":"Usuario no eliminado"}
    return {"message":"Usuario eliminado"}
            




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no encontrado"}
    


    