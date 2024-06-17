from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Editorial, Author, Book
from schemas import (
    EditorialCreateSchema,
    EditorialSchema,
    AuthorCreateSchema,
    AuthorSchema,
    BookCreateSchema,
    BookSchema,
)


def editorials_show(db: Session):
    return db.query(Editorial)


def editorial_select(db: Session, editorial_id: int):
    select_editorial = db.get(Editorial, editorial_id)
    if not select_editorial:
        raise HTTPException(status_code=404, detail="Id not exit")
    return db.query(Editorial).filter(Editorial.id == editorial_id).first()


def editorial_create(db: Session, editorial: EditorialCreateSchema) -> EditorialSchema:
    db_editorial = Editorial(name=editorial.name)
    db.add(db_editorial)
    db.commit()
    db.refresh(db_editorial)
    return db_editorial


def editorial_update(db: Session, editorial_id: int,  editorial: EditorialCreateSchema) -> EditorialSchema:
    # Buscar en la BD el editorial por el id que recibido
    obj_editorial = db.query(Editorial).filter(Editorial.id == editorial_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_editorial.first() is None:
        raise HTTPException(status_code=404, detail="Editorial not found")
    # TransformAR los datos recibidos para que lo entienda la BD
    datas = editorial.model_dump(exclude_unset=True)
    # Actualizar el objeto
    obj_editorial.update(datas)
    # Guardar los cambios en BD
    db.commit()
    return obj_editorial.first()


def editorial_delete(db: Session, editorial_id: int) -> None:
    # Buscar en la BD el editorial por el id que recibido
    obj_editorial = db.query(Editorial).filter(Editorial.id == editorial_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_editorial.first() is None:
        raise HTTPException(status_code=404, detail="Editorial not found")
    # Borrar el objeto (si se ha encontrado la Id)
    obj_editorial.delete()
    # Guardar los cambios en BD
    db.commit()
    return None


def author_show(db: Session):
    return db.query(Author)


def author_select(db: Session, author_id: int):
    select_author = db.get(Author, author_id)
    if not select_author:
        raise HTTPException(status_code=404, detail="Id not exit")
    return db.query(Author).filter(Author.id == author_id).first()


def author_create(db: Session, author: AuthorCreateSchema) -> AuthorSchema:
    db_author = Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def author_update(db: Session, author_id: int,  author: AuthorCreateSchema) -> AuthorSchema:
    # Buscar en la BD el author por el id que recibido
    obj_author = db.query(Author).filter(Author.id == author_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_author.first() is None:
        raise HTTPException(status_code=404, detail="Author not found")
    # Transformar los datos recibidos para que lo entienda la BD
    datas = author.model_dump(exclude_unset=True)
    # Actualizar el objeto
    obj_author.update(datas)
    # Guardar los cambios en BD
    db.commit()
    return obj_author.first()


def author_delete(db: Session, author_id: int) -> None:
    # Buscar en la BD el author por el id que recibido
    obj_author = db.query(Author).filter(Author.id == author_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_author.first() is None:
        raise HTTPException(status_code=404, detail="Author not found")
    # Borrar el objeto (si se ha encontrado la Id)
    obj_author.delete()
    # Guardar los cambios en BD
    db.commit()
    return None


def book_show(db: Session):
    return db.query(Book)


def book_select(db: Session, book_id: int):
    select_book = db.get(Book, book_id)
    if not select_book:
        raise HTTPException(status_code=404, detail="Id not exit")
    return db.query(Book).filter(Book.id == book_id).first()


def book_create(db: Session, book: BookCreateSchema) -> BookSchema:
    select_editorial = db.get(Editorial, book.editorial_id)
    if not select_editorial:
        raise HTTPException(status_code=404, detail="Id Editorial not exit")
    select_author = db.get(Author, book.author_id)
    if not select_author:
        raise HTTPException(status_code=404, detail="Id Author not exit")
    db_book = Book(
        title=book.title,
        page=book.page,
        edition_date=book.edition_date,
        editorial_id=book.editorial_id,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def book_update(db: Session, book_id: int,  book: BookCreateSchema) -> BookSchema:
    # Buscar en la BD el book por el id que recibido
    obj_book = db.query(Book).filter(Book.id == book_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_book.first() is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # Transformar los datos recibidos para que lo entienda la BD
    datas = book.model_dump(exclude_unset=True)
    # Actualizar el objeto
    obj_book.update(datas)
    # Guardar los cambios en BD
    db.commit()
    return obj_book.first()


def book_delete(db: Session, book_id: int) -> None:
    # Buscar en la BD el book por el id que recibido
    obj_book = db.query(Book).filter(Book.id == book_id)
    # Si no encuentro el objeto en base de datos doy una excepción
    if obj_book.first() is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # Borrar el objeto (si se ha encontrado la Id)
    obj_book.delete()
    # Guardar los cambios en BD
    db.commit()
    return None
