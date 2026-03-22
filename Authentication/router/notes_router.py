from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user

router = APIRouter()

notes = []


# 🔹 CREATE
@router.post("/notes")
def create_note(content: str, user = Depends(get_current_user)):

    note = {
        "id": len(notes),
        "user": user.username,
        "content": content
    }

    notes.append(note)

    return note


# 🔹 GET ALL
@router.get("/notes")
def get_notes(user = Depends(get_current_user)):

    return [n for n in notes if n["user"] == user.username]


# 🔹 GET ONE
@router.get("/notes/{note_id}")
def get_note(note_id: int, user = Depends(get_current_user)):

    for note in notes:
        if note["id"] == note_id and note["user"] == user.username:
            return note

    raise HTTPException(status_code=404, detail="Note not found")


# 🔹 DELETE
@router.delete("/notes/{note_id}")
def delete_note(note_id: int, user = Depends(get_current_user)):

    for i, note in enumerate(notes):
        if note["id"] == note_id and note["user"] == user.username:
            notes.pop(i)
            return {"message": "Deleted"}

    raise HTTPException(status_code=404, detail="Not found")