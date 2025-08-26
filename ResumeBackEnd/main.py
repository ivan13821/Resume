import json
import os
from fastapi import FastAPI, Request
from logics.profile import Profile
from logics.help import Help
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()


#Для локального запуска
# path_to_start_project = "/home/ivashka/"

#для докера
path_to_start_project = "/app/"

front = Jinja2Templates(directory=f"{path_to_start_project}ResumeFront")
app.mount("/static", StaticFiles(directory=f"{path_to_start_project}ResumeFront"), name="front")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/profile/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_profile(login)
    if 'error' in data.keys():
        return front.TemplateResponse(
        "errors/not_found_profile/not_found_profile.html",
        {"request": request}
    )
    return front.TemplateResponse(
        "profile/profile.html",
        {"request": request, "photo_url":f"/static/profile_photo/{login}.jpg", **data}
    )




@app.get("/profile_get_skills/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_skills(login)
    return data




@app.get("/profile_get_books/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_books(login)
    return data




@app.get("/profile_get_experience/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_experience(login)
    return data




@app.get("/profile_get_works/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_works(login)
    return data



@app.get("/profile_get_education/{login}")
async def profile(login, request: Request):
    """Передает информацию о профиле пользователя"""

    data = Profile.get_education(login)
    return data



@app.get("/help")
async def help():
    """Передает информацию для помощи, а также основные правила и логику"""
    return Help.get_rules()






if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True  # опционально: автоматическая перезагрузка при изменениях
    )