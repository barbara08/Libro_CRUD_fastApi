from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# http://127.0.0.1:8000/docs

class Book(BaseModel):
    title: str
    author: str
    editorial: int
    page: int

# Dictionary => all_books = book.dict()
    #{'title': 'aa', 'author': 'dd', 'editorial': 20, 'page': 70}
# Object => all_books = []
    #[Book(title='nn', author='xx', editorial=20, page=10)]

all_books = []

@app.post('/')
def insert_book(book: Book):
    #all_books.append(book)
    books = book.dict()
    all_books.append(books)
    print(all_books)
    return {"Book insert correctly"}

@app.get('/')
def show_book():
    #print(all_books)
    return (all_books)
    #return [x.model_dump() for x in all_books]

@app.delete('/{title}')
def delete_book(title):
    for position, item in enumerate(all_books):
        if item.title == title:
            all_books.pop(position)
            return {"Book deleted successfully"}
    return {"Book not found"}




if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
