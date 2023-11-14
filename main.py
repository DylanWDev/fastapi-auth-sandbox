from fastapi import FastAPI
import models
from database import engine
import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router, prefix="/game", tags=["game"])