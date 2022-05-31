from typing import List, Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str


class ItemCreate(ItemBase):
    income: int


class AddExpense(ItemBase):
    expense: int


class Item(ItemBase):
    id: int
    income: int
    balance: int

    class Config:
        orm_mode = True
