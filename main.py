from typing import Union
import schemas 
from fastapi import FastAPI
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
##using ready tool, called fastapi-crudrouter
class Four_fields(BaseModel):
    id: int
    size: int
    mass: float
    name: str
    surname: str

app = FastAPI()
app.include_router(CRUDRouter(schema=Four_fields))

##first try 
class Item(BaseModel):
    name: str
    surname: str
    height: float 
    weight: float
    is_offer: Union[bool, None] = None


fakeDatabase={
    1:{'task':'Clean car'},
    2:{'task':'be a good man'},
    3:{'task':'test'}
}

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]

@app.get("/")
def getALLItem(id:int):
    return fakeDatabase

#Option # 1
@app.post("/")
def addItem(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":task}
    return fakeDatabase


@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    fakeDatabase[id]['task'] = item.task 
    return fakeDatabase

@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase