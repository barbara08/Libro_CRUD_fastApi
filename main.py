from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# http://127.0.0.1:8000/docs

class Book(BaseModel):
    id: int
    title: str
    author: str
    editorial: str
    page: int

# Dictionary => all_books = book.dict()
    #{'title': 'aa', 'author': 'dd', 'editorial': 20, 'page': 70}
# Object => all_books = []
    #[Book(title='nn', author='xx', editorial=20, page=10)]

all_books = {}

#book1 = Book(id=0, title= "popo", author="gg", editorial="sm", page=99)
#all_books[book1.id] = book1
#book2 = Book(id=1, title= "popo", author="gg", editorial="sm", page=99)

@app.post('/')
def insert_book(book: Book):
    all_books[book.id] = book
    print(all_books)
    return {"Book insert correctly"}

@app.get('/')
def show_book():
    #print(all_books)
    return (all_books)
    #return [x.model_dump() for x in all_books]

@app.delete('/{id}')
def delete_book(id):
    if all_books[id] == id:
        all_books.pop(id)
        return {"Book deleted successfully"}
    return {"Book not found"}




if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
