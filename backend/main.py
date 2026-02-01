from backend.db import engine, Base
from backend.models.movie_model import Movie
from fastapi import FastAPI
from backend.api.movie_routes import router as movie_router
from backend.background.updater import start_background_task

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Movie API is running"}

app.include_router(movie_router)
start_background_task()
