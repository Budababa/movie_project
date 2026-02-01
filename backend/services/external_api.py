import os
import requests
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

class OMDbClient:
    BASE_URL = "http://www.omdbapi.com/"

    @classmethod
    def search_movie(cls, title: str):
        params = {
            "t": title,
            "apikey": OMDB_API_KEY
        }
        response = requests.get(cls.BASE_URL, params=params)
        if response.status_code != 200:
            return {"error": "OMDb API request failed"}
        data = response.json()
        if data.get("Response") == "False":
            return {"error": data.get("Error")}
        # Return relevant fields only
        return {
            "title": data.get("Title"),
            "year": int(data.get("Year", 0)) if data.get("Year") else 0,
            "genre": data.get("Genre", ""),
            "rating": float(data.get("imdbRating", 0.0)) if data.get("imdbRating") != "N/A" else 0.0,
            "poster_url": data.get("Poster", "")
        }
