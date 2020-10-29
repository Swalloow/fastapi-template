from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health
from app.db import database, engine, metadata

metadata.create_all(engine)
app = FastAPI(title="project_name", docs_url=None)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:8080",
]


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# application settings
app.include_router(health.router, prefix="/health", tags=["health"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
