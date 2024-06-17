import uvicorn

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from crud import (editorials_show,
                  editorial_select,
                  editorial_create,
                  editorial_update,
                  editorial_delete,
                  author_show,
                  author_select,
                  author_create,
                  author_update,
                  author_delete,
                  book_show,
                  book_select,
                  book_create,
                  book_update,
                  book_delete,
                  )

from schemas import (EditorialSchema, EditorialCreateSchema,
                     AuthorSchema, AuthorCreateSchema,
                     BookSchema, BookCreateSchema,
                     )

from database import Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

# http://127.0.0.1:8000/docs


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/editorials/", response_model=list[EditorialSchema])
def get_editorial(db: Session = Depends(get_db)):
    editorials = editorials_show(db)
    return editorials


@app.get("/editorials/{id}/", response_model=EditorialSchema)
def get_editorial_id(id: int, db: Session = Depends(get_db)):
    editorials = editorial_select(db, id)
    return editorials


@app.post("/editorials/", response_model=EditorialSchema)
def create_editorial(editorial: EditorialCreateSchema, db: Session = Depends(get_db)) -> EditorialSchema:
    new_editorial = editorial_create(db, editorial)
    return new_editorial


@app.put("/editorials/{id}", response_model=EditorialSchema)
def update_editorial(id: int, editorial: EditorialCreateSchema, db: Session = Depends(get_db)) -> EditorialSchema:
    new_update_editorial = editorial_update(db, id, editorial)
    return new_update_editorial


@app.delete("/editorials/{id}")  # response_model=EditorialSchema)
def delete_editorial(id: int, db: Session = Depends(get_db)):
    editorial_delete(db, id)
    return {"deleted Editorial"}


@app.get("/authors/", response_model=list[AuthorSchema])
def get_author(db: Session = Depends(get_db)):
    authors = author_show(db)
    return authors


@app.get("/authors/{id}", response_model=AuthorSchema)
def get_author_id(id: int, db: Session = Depends(get_db)):
    authors = author_select(db, id)
    return authors


@app.post("/authors/", response_model=AuthorSchema)
def create_author(author: AuthorCreateSchema, db: Session = Depends(get_db)) -> AuthorSchema:
    new_author = author_create(db, author)
    return new_author


@app.put("/authors/{id}", response_model=AuthorSchema)
def update_author(id: int, author: AuthorCreateSchema, db: Session = Depends(get_db)) -> AuthorSchema:
    new_update_author = author_update(db, id, author)
    return new_update_author


@app.delete("/authors/{id}")
def delete_author(id: int, db: Session = Depends(get_db)):
    author_delete(db, id)
    return {"deleted Author"}


@app.get("/books/", response_model=list[BookSchema])
def get_book(db: Session = Depends(get_db)):
    books = book_show(db)
    return books


@app.get("/books/{id}/", response_model=BookSchema)
def get_book_id(id: int, db: Session = Depends(get_db)):
    books = book_select(db, id)
    return books


@app.post("/books/", response_model=BookSchema)
def create_book(book: BookCreateSchema, db: Session = Depends(get_db)) -> BookSchema:
    new_book = book_create(db, book)
    return new_book


@app.put("/books/{id}", response_model=BookSchema)
def update_book(id: int, book: BookCreateSchema, db: Session = Depends(get_db)) -> BookSchema:
    new_update_book = book_update(db, id, book)
    return new_update_book


@app.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    book_delete(db, id)
    return {"deleted book"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
