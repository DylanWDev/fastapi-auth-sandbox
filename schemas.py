from typing import List, Optional, Generic, TypeVar
from datetime import date
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class GameSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    release_date: Optional[date]=None

    class Config:
        orm_mode = True


class GenreSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None


    class Config:
        orm_mode = True


class PlatformSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None


    class Config:
        orm_mode = True


class GameGenreSchema(BaseModel):
    game: Optional[GameSchema]=None
    genre: Optional[GameSchema]=None


    class Config:
        orm_mode = True


class GamePlatformSchema(BaseModel):
    game: Optional[GameSchema]=None
    platform: Optional[PlatformSchema]=None


    class Config:
        orm_mode = True