# Use this as the entery point for Apis
from io import StringIO
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, FastAPI, HTTPException, UploadFile
import  models
from database import SessionLocal, engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
# Database session creation
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Post request for uploading the file
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, db: Session = Depends(get_db)):
    print(file)
    print(file.filename)
    # Reading the uploaded file
    contents = file.file.read()
    # Converting the uploaded file content in string *** TODO :- Find a better and standard way to store the file content
    data = str(contents)
    # Inserting file content in file table in DB
    db_user = models.File(filename=file.filename,user_ids=[],content=data )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


