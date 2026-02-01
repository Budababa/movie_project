# Movie Database Project

## Rövid bemutatás

Ez a projekt egy mikroszerviz-alapú Python rendszer, amely lehetővé teszi filmek kezelését és megjelenítését.
A rendszer a következő fő funkciókat tartalmazza:

* Filmek listázása az adatbázisból
* Film keresése az OMDb API-n keresztül
* Film hozzáadása a saját adatbázishoz
* Vizualizáció: filmek értékelései diagramon

A projekt bemutatja a **procedurális, funkcionális és objektumorientált programozási elemeket**, valamint **REST API, Streamlit frontend, aszinkron feldolgozás és automatizált feladatok** használatát.

---

## Architektúra

```
movie_project/
│
├─ backend/
│  ├─ main.py              # FastAPI app entrypoint
│  ├─ api/                 # API végpontok
│  ├─ models/              # SQLAlchemy modellek
│  └─ services/            # Üzleti logika
│
├─ frontend/
│  └─ app.py               # Streamlit frontend
│
├─ tests/                  # Pytest tesztek
├─ requirements.txt        # Függőségek
└─ README.md
```

---

## Követelmények

* Python 3.13+
* Függőségek: `fastapi`, `uvicorn`, `streamlit`, `sqlalchemy`, `pydantic`, `requests`, `beautifulsoup4`, `python-dotenv`, `pytest`, `pandas`

Telepítés virtuális környezetben:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Indítás

### Backend

```bash
cd backend
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
streamlit run app.py
```

> **Fontos:** A frontend a backend URL-jét environment variable-ból olvassa:
>
> ```bash
> export BACKEND_URL=https://movie-project-58bs.onrender.com  # Linux/Mac
> setx BACKEND_URL "https://movie-project-58bs.onrender.com"   # Windows
> ```

---

## Deploy linkek

* **Frontend (Streamlit Cloud):** [[itt add meg a linket](https://realmultiparadigma.streamlit.app)]
* **Backend (Render):** [[itt add meg a linket](https://movie-project-58bs.onrender.com)]

---

## Tesztelés

* Egységtesztek a `tests/` mappában találhatók
* Futtatás:

```bash
pytest
```

* Legalább három teszt van, egyik `@pytest.mark.parametrize` használatával

---

## Bemutató

* Backend végpontok bemutatása: `/movies`, `/search`, `/search_and_add`
* Frontend működés bemutatása: film lista, keresés, hozzáadás, rating diagram
