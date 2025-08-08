from fastapi import FastAPI, Request
from logics.profile import Profile
from logics.help import Help
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import time

app = FastAPI()
front = Jinja2Templates(directory="/home/ivashka/Resume/ResumeFront")
app.mount("/static", StaticFiles(directory="/home/ivashka/Resume/ResumeFront"), name="front")

@app.get("/profile/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_profile(login)
    if 'error' in data.keys():
        return data
    return front.TemplateResponse(
        "profile.html",
        {"request": request, "photo_url":f"/static/profile_photo/{login}.jpg", **data}
    )


@app.get("/profile_get_skills/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_skills(login)
    print(data)
    return data




@app.get("/help")
async def help():
    """Передает информацию для помощи, а также основные правила и логику"""
    return Help.get_rules()





