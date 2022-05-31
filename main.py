from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models.models
import schemas.schemas
import database

models.models.database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.schemas.Item)
def create_user(user: schemas.schemas.ItemCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.schemas.Item])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.schemas.Item)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/expense/", response_model=schemas.schemas.Item)
def add_expense(user: schemas.schemas.AddExpense, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    return crud.add_expense(db=db, user=user)