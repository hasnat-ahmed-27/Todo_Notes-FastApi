from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NoteCreate(BaseModel):
    """Schema for creating a new note."""
    title: str = Field(..., min_length=1, max_length=200, description="Title of the note")
    content: str = Field(..., min_length=1, description="Content/body of the note")
    tags: Optional[list[str]] = Field(default=[], description="Optional list of tags")


class NoteUpdate(BaseModel):
    """Schema for partially updating a note (all fields optional)."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    tags: Optional[list[str]] = None


class NoteResponse(BaseModel):
    """Schema for note data returned to the client."""
    id: str
    title: str
    content: str
    tags: list[str]
    created_at: datetime
    updated_at: datetime


class MessageResponse(BaseModel):
    """Generic message response."""
    message: str


class ErrorResponse(BaseModel):
    """Error response schema."""
    detail: str
    status_code: int
