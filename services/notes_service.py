from typing import Optional
from fastapi import HTTPException, status

from models.note_model import Note
from schemas.note_schema import NoteCreate, NoteUpdate


# In-memory store: { note_id: Note }
_notes_store: dict[str, Note] = {}


def create_note(payload: NoteCreate) -> Note:
    """Create a new note and persist it in the store."""
    note = Note(
        title=payload.title,
        content=payload.content,
        tags=payload.tags or [],
    )
    _notes_store[note.id] = note
    return note


def get_all_notes() -> list[Note]:
    """Return all notes sorted by creation time (newest first)."""
    return sorted(_notes_store.values(), key=lambda n: n.created_at, reverse=True)


def get_note_by_id(note_id: str) -> Note:
    """Fetch a single note by ID. Raises 404 if not found."""
    note = _notes_store.get(note_id)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note with id '{note_id}' not found.",
        )
    return note


def update_note(note_id: str, payload: NoteUpdate) -> Note:
    """Partially update a note. Only fields provided in payload are changed."""
    note = get_note_by_id(note_id)
    note.update(
        title=payload.title,
        content=payload.content,
        tags=payload.tags,
    )
    return note


def delete_note(note_id: str) -> None:
    """Delete a note by ID. Raises 404 if not found."""
    get_note_by_id(note_id)  # will raise 404 if missing
    del _notes_store[note_id]


def search_notes(query: str) -> list[Note]:
    """Search notes by title or content (case-insensitive)."""
    q = query.lower()
    results = [
        note for note in _notes_store.values()
        if q in note.title.lower() or q in note.content.lower()
    ]
    return sorted(results, key=lambda n: n.created_at, reverse=True)
