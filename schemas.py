from typing import Optional
from pydantic import BaseModel
from datetime import date

class GameSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    release_date: Optional[date] = None

    class Config:
        orm_mode = True

class GenreSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True

class PlatformSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True

class GameGenreSchema(BaseModel):
    game: Optional[GameSchema] = None
    genre: Optional[GenreSchema] = None

    class Config:
        orm_mode = True

class GamePlatformSchema(BaseModel):
    game: Optional[GameSchema] = None
    platform: Optional[PlatformSchema] = None

    class Config:
        orm_mode = True
