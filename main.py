from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from google.cloud import firestore
from firestore.get_item import get_item

general_pages_router = APIRouter()

db = firestore.Client(project="brt-svc-data-platform-dev")

@general_pages_router.get("/source/{item_id}")
async def home(item_id: str, request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("interface.html", {"request": request,
                                                         "video_title": "Video title",
                                                         "page_title": "Page Title",
                                                         "description": "Video description"})
