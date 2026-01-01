from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .data import movies
from .knn import recommend_knn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sessão em memória (avaliacoes)
ratings = {}

# Avaliar filme ⭐
@app.post("/api/rate")
def rate(data:dict):
    ratings[data["filme"]] = int(data["nota"])
    return {"status":"ok","total_avaliados":len(ratings)}

# Recomendar
@app.get("/api/recommend")
def recommend():
    if not ratings:
        return []
    return recommend_knn(ratings, movies)

# Frontend
app.mount("/app", StaticFiles(directory="api/static", html=True), name="static")
