# from random import sample
# from telnetlib import STATUS
from typing import Optional
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()
class postparam(BaseModel):
    item: str
    content:str
    status: bool =True
    rating: Optional[int] =None
    

temparraydatabase =[{" item ":" Book "," content ":" unruled Books "},{" item ":" Pen "," content ":" Ball pen "}]

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
@app.post("/createposts")
def post(postings:postparam):
    asdic = postings.dict()
    asdic['id'] = randrange(0,100000)
    temparraydatabase.append(asdic)
    return {"data": temparraydatabase}
        