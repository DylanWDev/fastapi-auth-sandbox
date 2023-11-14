from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    genres = relationship("Genre", secondary="game_genres")
    platforms = relationship("Platform", secondary="game_platforms")

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class GameGenre(Base):
    __tablename__ = "game_genres"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    game = relationship("Game", back_populates="game_genres")
    genre = relationship("Genre", back_populates="game_genres")

class GamePlatform(Base):
    __tablename__ = "game_platforms"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))

    game = relationship("Game", back_populates="game_platforms")
    platform = relationship("Platform", back_populates="game_platforms")

Game.game_genres = relationship("GameGenre", order_by=GameGenre.id, back_populates="game")
Game.game_platforms = relationship("GamePlatform", order_by=GamePlatform.id, back_populates="game")
Genre.game_genres = relationship("GameGenre", order_by=GameGenre.id, back_populates="genre")
Platform.game_platforms = relationship("GamePlatform", order_by=GamePlatform.id, back_populates="platform")
