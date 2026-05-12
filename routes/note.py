from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", ""),
            "description": doc.get("description", ""),
            "highpriority": doc.get("highpriority", False)
        })
    return templates.TemplateResponse(request, "index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = {
        "title": form.get("title"),
        "description": form.get("description"),
        "highpriority": form.get("highpriority") == "on"
    }
    note_obj = conn.notes.notes.insert_one(formDict)
    return RedirectResponse(url="/", status_code=303) 