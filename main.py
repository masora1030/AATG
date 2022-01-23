from fastapi import FastAPI, HTTPException
from utils.aatg import AATG

from fastapi.responses import HTMLResponse

from pydantic import BaseModel

# pydantic model
class TitleIn(BaseModel):
    original_title: str

class TitleOut(TitleIn):
    av_title: str

app = FastAPI()
aatg = AATG()

@app.get("/", response_class=HTMLResponse)
async def open_homepage():
    html_content = '''
    <html>
        <head>
            <title>Hi Guys!</title>
        </head>
        <body>
            <h1>We have a gift for you!</h1>
        </body>
    </html>
    '''
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/predict", response_model=TitleOut, status_code=200)
def get_prediction(payload: TitleIn, ngram_num=3):
    original_title = payload.original_title

    try:
        av_title = aatg.generate_title(original_title, ngram_num)
    except:
        raise HTTPException(status_code=400, detail="Can not generate AV")

    response_object = {"original_title": original_title, "av_title": av_title}
    return response_object
