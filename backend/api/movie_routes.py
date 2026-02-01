from fastapi import APIRouter
from backend.services.movie_service import MovieService
from backend.schemas.movie_schema import MovieCreate, MovieRead
from typing import List
from backend.services.external_api import OMDbClient
import os

router = APIRouter()

service = MovieService()

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
