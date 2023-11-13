from fastapi import FastAPI
from database import engine
from sqlalchemy import select
from fastapi.response import PlainTextResponse
from starlette.exception import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
import models

app = FastAPI()

# origins = [
#     ""
# ]

@app.get("/")
async def root():
    return {"message": "Hello World"}
