from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from utils.aatg import AATG

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

aatg = AATG()

templates = Jinja2Templates(directory="")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def get_prediction(request: Request, original_title: str = Form(...), ero_level: int = Form(...)):

    try:
        av_title = aatg.generate_title(original_title,float(ero_level) / 100)
    except:
        raise HTTPException(status_code=400, detail="Can not generate AV")

    original_title.replace(' ', '　')

    tweet_url = f"https://twitter.com/share?text={original_title}%0a↓%0a↓%0a↓%0a{av_title}%0a%23AutoAvTitleGenerator%0ahttps://aatgavlove.herokuapp.com%0a&count=none&lang=ja"
    context = {"request": request, "original_title": original_title, "av_title": av_title, "tweet_url": tweet_url}
    return templates.TemplateResponse("result.html", context)
