import pytest
from backend.services.movie_service import MovieService
from backend.schemas.movie_schema import MovieCreate

@pytest.fixture
def service():
    service = MovieService()
    yield service
    service.close()

def test_create_and_get_movie(service):
    movie_data = MovieCreate(title="Test Movie", year=2023, genre="Action", rating=7.5)
    movie = service.create_movie(movie_data)

    fetched = service.get_movie(movie.id)
    assert fetched.title == "Test Movie"
    assert fetched.rating == 7.5

def test_get_movies_list(service):
    movies = service.get_movies()
    assert isinstance(movies, list)

@pytest.mark.parametrize("rating_input, expected", [
    ([7.0, 8.0, 9.0], 8.0),
    ([5.5, 6.5], 6.0)
])
def test_average_rating(rating_input, expected):
    avg = sum(rating_input) / len(rating_input)
    assert avg == expected
