import streamlit as st
import requests
import pandas as pd
import os

BACKEND_URL = os.getenv("BACKEND_URL", "https://movie-project-58bs.onrender.com")

st.title("Movie Database")

# --- Film keresés és mentés ---
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
            
            if st.button("Add to DB"):
                post_resp = requests.post(f"{BACKEND_URL}/search_and_add", params={"title": search_title})
                st.success(f"Added: {post_resp.json()['title']}")

# --- Film lista ---
st.header("All Movies")
response = requests.get(f"{BACKEND_URL}/movies")
movies = response.json()
if movies:
    df = pd.DataFrame(movies)
    st.dataframe(df)
    
    # --- Vizualizáció: rating diagram ---
    st.header("Ratings Chart")
    st.bar_chart(df.set_index("title")["rating"])
else:
    st.info("No movies in database yet.")
