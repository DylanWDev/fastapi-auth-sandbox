from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import GameSchema
from database import SessionLocal
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create_game(request: GameSchema, db: Session = Depends(get_db)):
    return crud.create_game(db, request)

@router.get('/get/{game_id}')
async def get_game(game_id: int, db: Session = Depends(get_db)):
    return crud.get_game_by_id(db, game_id)

@router.get('/list/')
async def list_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_game(db, skip=skip, limit=limit)

@router.put('/update/{game_id}')
async def update_game(game_id: int, title: str, release_date: date, db: Session = Depends(get_db)):
    return crud.update_game(db, game_id, title, release_date)

@router.delete('/delete/{game_id}')
async def delete_game(game_id: int, db: Session = Depends(get_db)):
    return crud.delete_game(db, game_id)
