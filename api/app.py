from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .data import movies
from .knn import knn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API FIRST
@app.post("/api/recommend")
def recommend(prefs:dict):
    user=[prefs["violencia"],prefs["romance"],prefs["acao"],prefs["comedia"]]
    return knn(user, movies)

# Frontend AFTER
app.mount("/app", StaticFiles(directory="api/static", html=True), name="static")
