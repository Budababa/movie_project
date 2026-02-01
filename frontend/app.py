import streamlit as st
import requests
import pandas as pd
import os

BACKEND_URL = os.getenv("BACKEND_URL", "https://movie-project-58bs.onrender.com")

st.title("Movie Database")

# --- Session State inicializálása ---
if "movies" not in st.session_state:
    st.session_state.movies = []

if "last_search" not in st.session_state:
    st.session_state.last_search = None

# --- Film lista betöltése az adatbázisból, ha üres a session state ---
if not st.session_state.movies:
    response = requests.get(f"{BACKEND_URL}/movies")
    if response.ok:
        st.session_state.movies = response.json()

# --- Film keresés ---
st.header("Search Movie (OMDb)")
search_title = st.text_input("Enter movie title:")

if st.button("Search"):
    if search_title.strip() != "":
        response = requests.get(f"{BACKEND_URL}/search", params={"title": search_title})
        data = response.json()
        if "error" in data:
            st.error(data["error"])
            st.session_state.last_search = None
        else:
            st.session_state.last_search = data  # mentjük session state-be
            st.write("Movie found:")
            st.json(data)

# --- Hozzáadás az adatbázishoz ---
if st.session_state.last_search:
    if st.button("Add to DB"):
        post_resp = requests.post(
            f"{BACKEND_URL}/search_and_add",
            json={"title": st.session_state.last_search["title"]}
        )
        data = post_resp.json()
        if data.get("title"):
            st.success(f"Added: {data['title']}")
            # Frissítjük a teljes film listát az adatbázisból
            response = requests.get(f"{BACKEND_URL}/movies")
            if response.ok:
                st.session_state.movies = response.json()
            st.session_state.last_search = None
        else:
            st.error("Failed to add movie")

# --- Film lista megjelenítése ---
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
