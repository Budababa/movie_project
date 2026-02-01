import threading
import time
import schedule
from backend.services.movie_service import MovieService
from backend.services.external_api import OMDbClient

def update_movie_ratings():
    service = MovieService()
    movies = service.get_movies()
    for movie in movies:
        data = OMDbClient.search_movie(movie.title)
        if "rating" in data:
            movie.rating = data["rating"]
    service.db.commit()
    service.close()
    print("Movie ratings updated!")

def run_scheduler():
    schedule.every(1).minutes.do(update_movie_ratings)  # teszteléshez 1 perc, deploynál lehet naponta

    while True:
        schedule.run_pending()
        time.sleep(1)

# Futtatás külön szálon
def start_background_task():
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
