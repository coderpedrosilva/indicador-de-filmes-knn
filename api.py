from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import movies
from knn import knn

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_methods=["*"],
 allow_headers=["*"],
)

@app.post("/recommend")
def recommend(prefs:dict):
    user = [prefs["violencia"],prefs["romance"],prefs["acao"],prefs["comedia"]]
    return knn(user, movies)
