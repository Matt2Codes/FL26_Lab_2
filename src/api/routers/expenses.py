from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from api.database import get_session
from api.models import ExpenseCreate, ExpenseRead

router = APIRouter()

# TODO (Week 7): Implement expense creation, listing, split, and reports via tasks.md
