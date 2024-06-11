from fastapi import FastAPI
import uvicorn

from book import Book
from editorial import list_editorial


all_books = {}


@app.post('/')
def insert_book(book: Book):
    # LLAMAR A LA BBDD
    all_books[book.id] = book
    print(all_books)
    return {"Book insert correctly"}


@app.get('/')
def show_book():
    # print(all_books)
    return (all_books)
    # return [x.model_dump() for x in all_books]


@app.delete('/{id}')
def delete_book(id):
    if all_books[id] == id:
        all_books.pop(id)
        return {"Book deleted successfully"}
    return {"Book not found"}


# crud editorial
@app.get('/editorial')
def get_editorial(self):
    return list_editorial()


if __name__ == "__main__":
    uvicorn.run("antiguo_main:app", port=8000, reload=True)
