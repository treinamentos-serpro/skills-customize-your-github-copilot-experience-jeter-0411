from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: dict[int, Book] = {}
next_book_id = 1
