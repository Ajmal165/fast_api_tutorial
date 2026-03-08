from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://new_user_fast_api:G4z11b5ymUnKvBR0@cluster1.ibryvvz.mongodb.net/notes")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "description": doc["description"],
            "important": doc["important"],
        })

    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@app.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    formDict["important"] = True if formDict["important"] == "on" else False

    conn.notes.notes.insert_one(formDict)

    return {"success": True}



@app.get("/items/{item_id}")
async def read_item(item_id : int, q: str | None = None):
    print("ajmal")
    return {"item_id": item_id, "q": q}


