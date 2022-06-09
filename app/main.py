
# from webbrowser import get
from fastapi import  Depends, FastAPI,Response,status,HTTPException

from pydantic import BaseModel

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from database import Base,SessionLocal
from database import get_db

#create db

from database import Base,engine
from models import Item

# print("Creating database ....")

Base.metadata.create_all(engine)

# from requests import Response
app = FastAPI()
# db = SessionLocal()
get_db()


class postparam(BaseModel):
    id:int
    title: str
    content:str
    Published: bool
    class Config:
        orm_mode =True


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

    

@app.get("/sql")
async def root(db:Session=Depends(get_db)):
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
    cursor.execute("""SELECT * FROM "Products" WHERE id = %s ;""",(str(id),))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"id:{id} was not found.Thankyou for searching" )
    return {"posts detail": post}

# delete post is must
@app.delete("/profile/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int):
    cursor.execute("""DELETE FROM "Products" WHERE id = %s returning *""",(str(id),))
    delete_post=cursor.fetchone()
    conn.commit()
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The element with {id} id does not exist")
    return Response(status_code= status.HTTP_204_NO_CONTENT)   


@app.put("/profile/{id}")
def update_posts(id:int,post:postparam):
    cursor.execute("""UPDATE "Products" SET title=%s ,content=%s ,published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.Published,str(id)))
    updated_data = cursor.fetchone()
    conn.commit()
    if updated_data==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} donot exist")   
  
    return {"data":updated_data}