from sqlalchemy.orm import Session

import models.models
import schemas.schemas

schemas = schemas.schemas
models = models.models


def get_user(db: Session, user_id: int):
    return db.query(models.Budget).filter(models.Budget.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.Budget).filter(models.Budget.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Budget).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.ItemCreate):
	db_user = models.Budget(income=user.income, name=user.name, balance=user.income)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

def add_expense(db: Session, user: schemas.AddExpense):
	curr_expense = db.query(models.Budget).filter(models.Budget.name == user.name).first()
	curr_expense.expense += user.expense
	curr_expense.balance = curr_expense.income - curr_expense.expense
	db.add(curr_expense)
	db.commit()
	db.refresh(curr_expense)
	return curr_expense

