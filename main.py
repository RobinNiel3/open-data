from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/test")
async def home(request: Request):
    return templates.TemplateResponse("interface.html", {"request": request,
                                                         "title": "Video title",
                                                         "page_title": "Page Title",
                                                         "description": "Video description"})
