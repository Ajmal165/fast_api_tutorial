from fastapi import APIRouter
from models.note import Notes
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = list(conn.notes.notes.find({}))

    newDocs = []

    for doc in docs:
        newDocs.append({
            "id": str(doc.get("_id")),
            "title": str(doc.get("title")),
            "description": doc.get("description", ""),
            "important": doc.get("important", False)
        })

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "newDocs": newDocs}
    )


@router.post("/")
async def create_note(request: Request):
    form = await request.form()
    print("form========",form)
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"success": True}



# @router.post("/")
# def add_note(note: Notes):
#     print(note)
#     inserted_notes = conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_notes)
