import os

from dotenv import load_dotenv
from fastapi import FastAPI
from prometheus_client import Summary, start_http_server

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

app = FastAPI()

# Iniciar un servidor Prometheus en el puerto 8001
start_http_server(8001)

# Crear un resumen para el tiempo de ejecución
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")


@app.get("/")
@REQUEST_TIME.time()
def read_root():
    return {"message": "Welcome to Task Manager API"}


@app.get("/database-url")
@REQUEST_TIME.time()
def get_database_url():
    return {"database_url": os.getenv("DATABASE_URL")}
