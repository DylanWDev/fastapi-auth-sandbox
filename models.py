from sqlalchemy import Column, String, Integer, Date
from database import Base

class Game(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)