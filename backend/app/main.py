from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import Item

app = FastAPI()

# Autoriser le frontend à accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/")
def read_items():
    return [{"id": 1, "name": "Example Item"}]