from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from entities import Base

class Term(Base):
    __tablename__ = 'term'

    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, description: str):
        self.description = description