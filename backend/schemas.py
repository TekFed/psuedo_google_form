from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class FormCreate(BaseModel):
    title: str
    form_json: Dict[str, Any]

class FormUpdate(BaseModel):
    title: str
    form_json: Dict[str, Any]

class FormResponse(BaseModel):
    id: int
    title: str
    form_json: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True

class ResponseCreate(BaseModel):
    answers_json: Dict[str, Any]

class ResponseResponse(BaseModel):
    id: int
    form_id: int
    answers_json: Dict[str, Any]
    submitted_at: datetime

    class Config:
        from_attributes = True