from fastapi import FastAPI

from main import greet

app = FastAPI(title="Python Lab API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Python Lab API работает"}


@app.get("/greet/{name}")
def greet_by_name(name: str) -> dict[str, str]:
    return {"message": greet(name)}
