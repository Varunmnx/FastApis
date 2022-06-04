from typing import Optional
from fastapi import Body, FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
# from requests import Response
app = FastAPI()

class postparam(BaseModel):
    title: str
    content:str
    Published: bool =True
    
while True:
    try:
        conn = psycopg2.connect(host= 'localhost',database='FastApi',user='postgres',password='2580',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection Established!!')
        break
    except Exception as error:
        print("connection to database failed !!")
        print('Error: ',error)
        time.sleep(2)

    

temparraydatabase =[{" item ":" Book "," content ":" unruled Books ","id":1},{" item ":" Pen "," content ":" Ball pen ","id":2}]
def get_post(id):
    for element in temparraydatabase:
        if element['id'] == id:
             return element
        else:
            return None   
#returning the index of the element in the list to pop it from the list              
def find_index_post(id):
    for i,j in enumerate(temparraydatabase):
        if j['id'] == id:
            return i
        else:
            return None    


@app.get("/")
async def root():
    return {"message":"this is a sample fastapi"}
    #sample

@app.get("/posts")
async def profile():
    cursor.execute("""SELECT * FROM "Products"; """)
    posts = cursor.fetchall()
    return {"posts":posts}   



#post a data and giving unique id to each of the element saved
@app.post("/createposts")
def post(postings:postparam):
    cursor.execute("""INSERT INTO "Products" (title,content,published) VALUES(%s,%s,%s)""",(postings.title,postings.content,postings.Published))
    conn.commit()
    return {"created posts":"created posts"}

@app.get("/profile/{id}")
def get_posts(id:int):
    cursor.execute("""SELECT * FROM "Products" WHERE id = %s ;""",(str(id)))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"id:{id} was not found.Thankyou for searching" )
    return {"posts detail": post}

# delete post is must
@app.delete("/profile/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int):
    location = find_index_post(id)
    if location == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The element with such id does not exist")
    temparraydatabase.pop(location)
    return Response(status_code= status.HTTP_204_NO_CONTENT)   


@app.put("/profile/{id}")
def update_posts(id:int,post:postparam):
    index = find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} donot exist")   
    post_dict =post.dict()
    post_dict['id'] = id
    temparraydatabase[index] = post_dict
    return {"data":post_dict}