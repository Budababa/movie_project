import streamlit as st
import requests
import pandas as pd
import os

BACKEND_URL = os.getenv("BACKEND_URL", "https://movie-project-58bs.onrender.com")

st.title("Movie Database")

# --- Film keresés ---
st.header("Search Movie (OMDb)")
search_title = st.text_input("Enter movie title:")

if st.button("Search"):
    if search_title:
        response = requests.get(f"{BACKEND_URL}/search", params={"title": search_title})
        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.write("Movie found:")
            st.json(data)

            # --- Hozzáadás az adatbázishoz ---
            if st.button("Add to DB"):
                post_resp = requests.post(f"{BACKEND_URL}/search_and_add", params={"title": search_title})
                if post_resp.status_code == 200:
                    st.success(f"Added: {post_resp.json()['title']}")
                    
                    # --- Frissítjük a "All Movies" listát ---
                    all_movies_resp = requests.get(f"{BACKEND_URL}/movies")
                    movies = all_movies_resp.json()
                    if movies:
                        df = pd.DataFrame(movies)
                        display_columns = ["title", "year", "genre", "director", "rating"]
                        df = df[[col for col in display_columns if col in df.columns]]
                        st.dataframe(df)
                else:
                    st.error("Failed to add movie")

# --- Film lista --- (ha nem adtunk hozzá most)
st.header("All Movies")
if 'movies' not in locals():  # ha még nem frissítettük a listát a hozzáadás után
    response = requests.get(f"{BACKEND_URL}/movies")
    movies = response.json()
    if movies:
        df = pd.DataFrame(movies)
        display_columns = ["title", "year", "genre", "director", "rating"]
        df = df[[col for col in display_columns if col in df.columns]]
        st.dataframe(df)
    else:
        st.info("No movies in database yet.")

# --- Vizualizáció: rating diagram ---
if movies:
    if "rating" in df.columns:
        st.header("Ratings Chart")
        st.bar_chart(df.set_index("title")["rating"])
