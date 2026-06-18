from fastapi import APIRouter, status, Query
from typing import Optional

from schemas.note_schema import NoteCreate, NoteUpdate, NoteResponse, MessageResponse
import services.notes_service as notes_service

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate):
    """
    Create a new note.

    - **title**: Required. 1–200 characters.
    - **content**: Required. The body of the note.
    - **tags**: Optional list of string tags.
    """
    note = notes_service.create_note(payload)
    return note.to_dict()


@router.get("/", response_model=list[NoteResponse])
def get_all_notes(search: Optional[str] = Query(None, description="Search notes by title or content")):
    """
    Retrieve all notes (newest first).
    Pass ?search=keyword to filter by title or content.
    """
    if search:
        notes = notes_service.search_notes(search)
    else:
        notes = notes_service.get_all_notes()
    return [n.to_dict() for n in notes]


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: str):
    """
    Retrieve a single note by its ID.
    Returns 404 if the note does not exist.
    """
    note = notes_service.get_note_by_id(note_id)
    return note.to_dict()


@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, payload: NoteUpdate):
    """
    Partially update a note.
    Only fields included in the request body are changed.
    """
    note = notes_service.update_note(note_id, payload)
    return note.to_dict()


@router.delete("/{note_id}", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def delete_note(note_id: str):
    """
    Delete a note by its ID.
    Returns 404 if the note does not exist.
    """
    notes_service.delete_note(note_id)
    return {"message": f"Note '{note_id}' deleted successfully."}
