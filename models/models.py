from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import database

class Budget(database.Base):
    __tablename__ = "budget"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    income = Column(Integer)
    expense = Column(Integer, default=0)
    balance = Column(Integer)
