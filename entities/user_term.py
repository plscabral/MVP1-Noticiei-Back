from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from entities import Base

class UserTerm(Base):
    __tablename__ = 'user_term'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    term_id = Column(Integer, ForeignKey("term.id"))
    created_at = Column(DateTime, default=datetime.now())

    user = relationship("User", foreign_keys=user_id)
    term = relationship("Term", foreign_keys=term_id)

    def __init__(self, user_id: str, term_id: str):
        self.user_id = user_id
        self.term_id = term_id
