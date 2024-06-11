from sqlalchemy.orm import Session
# from . import models, schemas
from fastapi import Depends, FastAPI, HTTPException
from models import Editorial
from schemas import (
    # EditorialBaseSchema,
    EditorialCreateSchema,
    EditorialSchema,

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


"""
# read only one author

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

# read several authors


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

# read several books


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

# create datas


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def create_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(**book.model_dump(), owner_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
"""


"""
CREAR DATOS
Los pasos son:
- Cree una instancia de modelo SQLAlchemy con sus datos.
- add => ese objeto de instancia a su sesión de base de datos.
- commit => los cambios en la base de datos (para que se guarden).
- refresh =>su instancia (para que contenga cualquier dato nuevo 
de la base de datos, como el ID generado).

# Author
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, 
                    hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Book
# dict() => obsoleto en v2 => se usa model_dump()
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

    
https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_2

"""
