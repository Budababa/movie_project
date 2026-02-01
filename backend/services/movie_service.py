from backend.db import SessionLocal
from backend.models.movie_model import Movie
from backend.schemas.movie_schema import MovieCreate
import os

OMDB_API_KEY = os.getenv("OMDB_API_KEY")


class MovieService:
    def __init__(self):
        self.db = SessionLocal()

    def get_movies(self):
        movies = self.db.query(Movie).all()
        return movies

    def get_movie(self, movie_id: int):
        movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        return movie

    def create_movie(self, movie_data: MovieCreate):
        new_movie = Movie(
            title=movie_data.title,
            year=movie_data.year,
            genre=movie_data.genre,
            rating=movie_data.rating
        )
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)
        return new_movie

    def close(self):
        self.db.close()
