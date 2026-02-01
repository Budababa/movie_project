import os
import uvicorn
from fastapi import FastAPI
from backend.api.movie_routes import router as movie_router
from backend.db import engine, Base
from backend.models.movie_model import Movie
from backend.background.updater import start_background_task

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(movie_router)

# Background task
start_background_task()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
