from typing import Optional
from fastapi import Body, FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# from requests import Response
app = FastAPI()
class postparam(BaseModel):
    item: str
    content:str
    status: bool =True
    rating: Optional[int] =None
    

temparraydatabase =[{" item ":" Book "," content ":" unruled Books ","id":1},{" item ":" Pen "," content ":" Ball pen "}]
def get_post(id):
    for element in temparraydatabase:
        if element['id'] == id:
             return element
        else:
            return None     



@app.get("/")
async def root():
    return {"message":"this is a sample fastapi"}
    #sample

@app.get("/profile")
async def profile():
    return {"profile":"Varun Narayanan"}    
# using dict for data collection
# @app.post("/createposts")
# def post(sample:dict=Body):
#     return {"data":f"{sample['item']}and {sample['content']}"}

#post a data and giving unique id to each of the element saved
@app.post("/createposts")
def post(postings:postparam):
    asdic = postings.dict()
    asdic['id'] = randrange(0,100000)
    temparraydatabase.append(asdic)
    return {"data": temparraydatabase}

@app.get("/profile/{id}")
def get_posts(id:int):
    post = get_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"id:{id} was not found.Thankyou for searching" )
    return {"posts detail": post}