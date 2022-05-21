from random import sample
from fastapi import Body, FastAPI

app = FastAPI()

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