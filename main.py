import subprocess
subprocess.run('python -m unidic download')
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils.aatg import AATG

app = FastAPI()
aatg = AATG()

templates = Jinja2Templates(directory="")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def get_prediction(request: Request, original_title: str = Form(...), ero_level: int = Form(...), ngram_num: int = 3):

    try:
        av_title = aatg.generate_title(original_title, ngram_num, float(ero_level) / 100)
    except:
        raise HTTPException(status_code=400, detail="Can not generate AV")

    tweet_url = f"https://twitter.com/share?text={original_title}%0a↓%0a↓%0a↓%0a{av_title}%0a%23AutoAvTitleGenerator%0a&count=none&lang=ja"
    context = {"request": request, "original_title": original_title, "av_title": av_title, "tweet_url": tweet_url}
    return templates.TemplateResponse("result.html", context)
