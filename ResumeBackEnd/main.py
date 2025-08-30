
import os
from fastapi import FastAPI, Request
from logics.profile import Profile
from logics.help import Help
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import Response
import uvicorn

from config.env import Env

app = FastAPI()


front = Jinja2Templates(directory=f"{Env.start_patch()}ResumeFront")
app.mount("/static", StaticFiles(directory=f"{Env.start_patch()}ResumeFront"), name="front")


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/favicon.ico")
async def get_favicon():

    """Функция для получения фавикона"""

    path = f"{Env.start_patch()}ResumeBackEnd/favicon/favicon.ico"

    #При отсутствии фавикона не вызывает ошибки в браузере
    if not os.path.exists(path):
        print(f"Файл не найден: {os.path.abspath(path)}")
        return Response(status_code=204)

    return FileResponse(path)



@app.post("/profile/{login}")
async def profile(login: str):

    """Передает всю информацию о пользователе"""

    pass





@app.get("/profile/{login}")
async def profile(login: str, request: Request):

    """Передает информацию о профиле пользователя"""

    data = Profile.get_profile(login) # получение профиля пользователя по логину

    if 'error' in data.keys():
        return front.TemplateResponse(
        "errors/not_found_profile/not_found_profile.html",
        {"request": request}
    )

    return front.TemplateResponse(
        "profile/profile.html",
        {
            "request": request,
            "url": f"http://{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', 8000)}/",
            "photo_url": f"/static/profile_photo/{login}.jpg",
            **data
        }
    )




@app.get("/profile_get_skills/{login}")
async def profile(login: str):

    """Передает информацию о профиле пользователя"""

    data = Profile.get_skills(login) # Получение навыков
    return data




@app.get("/profile_get_books/{login}")
async def profile(login: str):

    """Передает информацию о профиле пользователя"""

    data = Profile.get_books(login)
    return data




@app.get("/profile_get_experience/{login}")
async def profile(login: str):

    """Передает информацию о навыках пользователя"""

    data = Profile.get_experience(login)
    return data




@app.get("/profile_get_works/{login}")
async def profile(login: str):

    """Передает информацию о опыте работы пользователя"""

    data = Profile.get_works(login)
    return data



@app.get("/profile_get_education/{login}")
async def profile(login):

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
        host=Env.host(),
        port = Env.port(),
        reload=False
    )