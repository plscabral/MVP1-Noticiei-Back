from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from entities import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(140))
    email = Column(String(140), unique=True)
    password = Column(String(10))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password