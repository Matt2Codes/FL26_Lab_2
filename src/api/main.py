from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from api.database import init_db
from api.routers import users, expenses


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    init_db()
    yield


app = FastAPI(
    title="Expense Tracker REST API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])


@app.get("/health", tags=["System"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
