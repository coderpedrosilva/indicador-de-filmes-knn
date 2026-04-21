from fastapi import FastAPI, Request, HTTPException
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

sessions: dict = {}

def get_session(request: Request) -> dict:
    session_id = request.headers.get("X-Session-Id", "default")
    if session_id not in sessions:
        sessions[session_id] = {}
    return sessions[session_id]

# Avaliar filme ⭐
@app.post("/api/rate")
def rate(data: dict, request: Request):
    if "filme" not in data or "nota" not in data:
        raise HTTPException(status_code=400, detail="Campos 'filme' e 'nota' são obrigatórios")
    nota = int(data["nota"])
    if nota < 1 or nota > 5:
        raise HTTPException(status_code=400, detail="Nota deve ser entre 1 e 5")
    ratings = get_session(request)
    ratings[data["filme"]] = nota
    return {"status":"ok","total_avaliados":len(ratings)}

# Recomendar
@app.get("/api/recommend")
def recommend(request: Request):
    ratings = get_session(request)
    if not ratings:
        return []
    return recommend_knn(ratings, movies)

# Frontend
app.mount("/app", StaticFiles(directory="api/static", html=True), name="static")
