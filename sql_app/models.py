from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Editorial(Base):
    __tablename__ = "editorial"

    id = Column(Integer, nullable=True, autoincrement="auto", primary_key=True)
    name = Column(String)


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
