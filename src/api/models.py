from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field


class Category(str, Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    UTILITIES = "utilities"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


# Database Table Model
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)


# API Request Schema
class UserCreate(SQLModel):
    name: str
    email: str


# API Response Schema
class UserRead(SQLModel):
    id: int
    name: str
    email: str


# Database Table Model for Expenses
class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: Decimal = Field(decimal_places=2, gt=Decimal("0.00"))
    category: Category
    description: str
    expense_date: date
    paid_by_id: int = Field(foreign_key="user.id")
    split_group_id: Optional[str] = Field(default=None, nullable=True)


class ExpenseCreate(SQLModel):
    amount: Decimal = Field(decimal_places=2, gt=Decimal("0.00"))
    category: Category
    description: str
    expense_date: date
    paid_by_id: int


class ExpenseRead(SQLModel):
    id: int
    amount: Decimal
    category: Category
    description: str
    expense_date: date
    paid_by_id: int
    split_group_id: Optional[str]
