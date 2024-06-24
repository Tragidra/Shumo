from os import name
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import user
from .config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Приложение запустилось"}


if name == "main":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)