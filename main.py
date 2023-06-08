from fastapi import APIRouter,FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from google.cloud import firestore
from firestore.get_item import get_item
from fastapi.staticfiles import StaticFiles



#general_pages_router = APIRouter()


db = firestore.Client(project="brt-svc-data-platform-dev")

def get_sources_hypertext(sources):
    final_str = "<ul>"
    for source in sources:
        final_str += f'<li><a href="{source}">{source}</a></li>'
    final_str += "</ul>"
    return final_str

app = FastAPI()

#app.include_router(general_pages_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/source/{item_id}")
async def home(item_id: str, request: Request):
    templates = Jinja2Templates(directory="templates")
    print(item_id)
    item = get_item(db, "sources", item_id)
    print(item)
    return templates.TemplateResponse("interface.html", {"request": request,
                                                         "video_title": item["title"],
                                                         "page_title": item["title"],
                                                         "description": get_sources_hypertext(item["sources"])})
