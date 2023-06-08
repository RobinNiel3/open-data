from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

general_pages_router = APIRouter()


@general_pages_router.get("/test")
async def home(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("interface.html", {"request": request,
                                                         "video_title": "Video title",
                                                         "page_title": "Page Title",
                                                         "description": "Video description"})
