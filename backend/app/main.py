from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import Item
from .api import router
from .database import create_db_and_tables

app = FastAPI()

# Autoriser le frontend à accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React + Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialiser la base de données au démarrage
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Inclure les routes de l'API
app.include_router(router)

# Route par défaut pour tester que l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "API is running"}