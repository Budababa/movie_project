from fastapi import APIRouter
from backend.services.movie_service import MovieService
from backend.schemas.movie_schema import MovieCreate, MovieRead
from typing import List
from backend.services.external_api import OMDbClient
from pydantic import BaseModel
from backend.schemas.movie_schema import MovieCreate
import os

router = APIRouter()

service = MovieService()

class MovieTitleRequest(BaseModel):
    title: str

@router.get("/movies", response_model=List[MovieRead])
def get_movies():
    return service.get_movies()

@router.get("/movies/{movie_id}", response_model=MovieRead)
def get_movie(movie_id: int):
    movie = service.get_movie(movie_id)
    if movie:
        return movie
    return {"error": "Movie not found"}

@router.post("/movies", response_model=MovieRead)
def create_movie(movie: MovieCreate):
    new_movie = service.create_movie(movie)
    return new_movie

@router.get("/search")
def search_movie(title: str):
    result = OMDbClient.search_movie(title)
    return result

@router.post("/search_and_add")
def search_and_add(movie_req: MovieTitleRequest):
    # Lekérjük az OMDb API-tól
    result = OMDbClient.search_movie(movie_req.title)
    if "error" in result:
        return {"error": result["error"]}

    # Alakítsuk át MovieCreate objektummá, mert a service ezt várja
    movie_create = MovieCreate(
        title=result["title"],
        year=result.get("year", 0),
        genre=result.get("genre", ""),
        rating=result.get("rating", 0.0)
    )

    try:
        # Mentés az adatbázisba
        new_movie = service.create_movie(movie_create)
        return {"title": new_movie.title}
    except Exception as e:
        return {"error": str(e)}