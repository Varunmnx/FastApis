from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"this is a sample fastapi"}
    #sample

@app.get("/profile")
async def profile():
    return {"profile":"Varun Narayanan"}    