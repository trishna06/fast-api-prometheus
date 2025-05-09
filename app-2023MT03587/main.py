from fastapi import FastAPI
import os
from dotenv import load_dotenv
from prometheus_fastapi_instrumentator import Instrumentator

load_dotenv()

app = FastAPI(
    title = os.getenv("APP_TITLE", "My FastAPI App"),
    version = os.getenv("APP_VERSION", "1.0")
)

app.podname = os.getenv("HOSTNAME", "Unknown Pod")

@app.get("/get_info")
def get_info():
    return {
        "APP_TITLE": app.title,
        "APP_VERSION": app.version,
        "POD_NAME": app.podname
    }

Instrumentator().instrument(app).expose(app)