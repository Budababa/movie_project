import streamlit as st
import requests
import pandas as pd
import os

BACKEND_URL = os.getenv("BACKEND_URL", "https://movie-project-58bs.onrender.com")

st.title("Movie Database")

# --- Film keresés ---
st.header("Search Movie (OMDb)")
search_title = st.text_input("Enter movie title:")

if 'movies' not in st.session_state:
    # alapértelmezett lekérés
    response = requests.get(f"{BACKEND_URL}/movies")
    st.session_state.movies = response.json() if response.ok else []

# --- Keresés és hozzáadás ---
if st.button("Search"):
    if search_title:
        response = requests.get(f"{BACKEND_URL}/search", params={"title": search_title})
        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.write("Movie found:")
            st.json(data)

            if st.button("Add to DB"):
                post_resp = requests.post(f"{BACKEND_URL}/search_and_add", params={"title": search_title})
                if post_resp.ok:
                    st.success(f"Added: {post_resp.json()['title']}")
                    # hozzáadjuk a session_state-hez, hogy azonnal látszódjon
                    st.session_state.movies.append(post_resp.json())
                else:
                    st.error("Failed to add movie")

# --- Film lista ---
st.header("All Movies")
if st.session_state.movies:
    df = pd.DataFrame(st.session_state.movies)
    display_columns = ["title", "year", "genre", "director", "rating"]
    df = df[[col for col in display_columns if col in df.columns]]
    st.dataframe(df)

    # --- Vizualizáció ---
    if "rating" in df.columns:
        st.header("Ratings Chart")
        st.bar_chart(df.set_index("title")["rating"])
else:
    st.info("No movies in database yet.")