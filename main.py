from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.config import Config

from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router

app = FastAPI()

config = Config(".env")
try:
    FE_AND_API_URL = config("FE_AND_API_URL")
    origins = list(FE_AND_API_URL.split(","))
    if len(origins) > 0:
        from starlette.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
except KeyError as e:
    print(type(e).__name__, e)
except Exception as e:
    print(type(e).__name__, e)


app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")
