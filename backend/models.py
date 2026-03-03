from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    form_json = Column(Text, nullable=False)          # stored as JSON string
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    responses = relationship("Response", back_populates="form", cascade="all, delete-orphan")


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"))
    answers_json = Column(Text, nullable=False)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    form = relationship("Form", back_populates="responses")