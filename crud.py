from sqlalchemy.orm import Session
from models import Game
from datetime import date
from schemas import GameSchema

def get_game(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Game).offset(skip).limit(limit).all()

def get_game_by_id(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()

def create_game(db: Session, game: GameSchema):
    _game = Game(title=game.title, release_date=game.release_date)
    db.add(_game)
    db.commit()
    db.refresh(_game)
    return _game

def delete_game(db: Session, game_id: int):
    _game = get_game_by_id(db=db, game_id=game_id)
    db.delete(_game)
    db.commit()

def update_game(db: Session, game_id: int, title: str, release: date):
    _game = get_game_by_id(db=db, game_id=game_id)
    _game.title = title
    _game.release_date = release
    db.commit()
    db.refresh(_game)
    return _game
