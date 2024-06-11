from pydantic import BaseModel


class EditorialBaseSchema(BaseModel):
    name: str


class EditorialCreateSchema(EditorialBaseSchema):
    pass


class EditorialSchema(EditorialBaseSchema):
    id: int

    class Config:
        orm_mode = True


"""
class BookBase(BaseModel):
    title: str
    page: int
    edition_dte: Date
    editorial_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    id: int
    name: str


class AuthorCreate(AuthorBase):
    # password: str   no tiene psw
    name: str


class Author(AuthorBase):
    id: int
    book: list[Book] = []

    class Config:
        orm_mode = True


"""
"""
EJEMPLO
#book
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

        ***

#author
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

"""
