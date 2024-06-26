from pydantic import BaseModel
from datetime import date


class EditorialBaseSchema(BaseModel):
    name: str


class EditorialCreateSchema(EditorialBaseSchema):
    pass


class EditorialSchema(EditorialBaseSchema):
    id: int

    class Config:
        orm_mode = True


class AuthorBaseSchema(BaseModel):
    # id: int
    name: str


class AuthorCreateSchema(AuthorBaseSchema):
    name: str


class AuthorSchema(AuthorBaseSchema):
    id: int
    # book: list[BookSchema] = []

    class Config:
        orm_mode = True


class BookBaseSchema(BaseModel):
    title: str
    page: int
    edition_date: date
    editorial_id: int
    author_id: int


class BookCreateSchema(BookBaseSchema):
    # title: str
    pass


class BookSchema(BookBaseSchema):
    id: int
    # editorial_id: int
    # author_id: int

    class Config:
        orm_mode = True
