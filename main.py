from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books.append(book)
    return book

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Book Library API",
        version="1.0.0",
        description="An API to manage books with FastAPI.",
        routes=app.routes,
    )
    openapi_schema["servers"] = [
        {"url": "https://fastapi-gpt-schema-example.onrender.com"}
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi