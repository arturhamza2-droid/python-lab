from fastapi import FastAPI
from pydantic import BaseModel, Field

from main import greet

app = FastAPI(title="Python Lab API")


class CalculateRequest(BaseModel):
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Python Lab API работает"}


@app.get("/greet/{name}")
def greet_by_name(name: str) -> dict[str, str]:
    return {"message": greet(name)}


@app.post("/calculate")
def calculate(request: CalculateRequest) -> dict[str, float | int]:
    return {
        "price": request.price,
        "quantity": request.quantity,
        "total": request.price * request.quantity,
    }
