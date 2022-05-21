# from random import sample
# from telnetlib import STATUS
from typing import Optional
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()
class postparam(BaseModel):
    item: str
    content:str
    status: True
    rating: Optional[int] =None


@app.get("/")
async def root():
    return {"message":"this is a sample fastapi"}
    #sample

@app.get("/profile")
async def profile():
    return {"profile":"Varun Narayanan"}    
# using dict for data collection
@app.post("/createposts")
def post(sample:dict=Body):
    return {"data":f"{sample['item']}and {sample['content']}"}
@app.post("/createpost")
def post(postings:postparam):
    return {"data":f"{postings.item} and content of that is {postings.content}"}
        