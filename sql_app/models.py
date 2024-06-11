from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Editorial(Base):
    __tablename__ = "editorial"

    id = Column(Integer, nullable=True, autoincrement="auto", primary_key=True)
    name = Column(String)

    # crear la relación, en este caso no la tiene, NO SE PONDRÁ NADA


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, nullable=True, autoincrement="auto", primary_key=True)
    name = Column(String)

    book = relationship("Book", back_populates="owner")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, nullable=True, autoincrement="auto", primary_key=True)
    title = Column(String, nullable=True)
    pages = Column(Integer, nullable=True)
    edition_date = Column(Date)
    editorial_id = Column(Integer, nullable=True)
    owner_id = Column(Integer, ForeignKey("author.id"))

    owner = relationship("Author", back_populates="book")


"""
PARA AUTHOR Y BOOK QUE TIENEN RELACION


EJEMPLO:
#author
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

#book
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
"""


"""
https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_2
"""
