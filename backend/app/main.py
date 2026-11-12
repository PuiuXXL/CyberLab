from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.engine import Engine

from app.api.health import router as health_router
from app.api.labs import router as labs_router
from app.api.auth import router as auth_router

from app.core.config import Settings
from app.db.connection import create_db_engine



def create_app(db_engine: Engine | None = None) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app : FastAPI):
        engine = db_engine
        if engine is None:
            engine = create_db_engine(Settings())


        app.state.db_engine = engine

        try:
            yield
        finally:
            if db_engine is None:
                engine.dispose()


    aplication = FastAPI(title = "CyberLab API", lifespan = lifespan)
    aplication.include_router(health_router)
    aplication.include_router(labs_router)
    aplication.include_router(auth_router)
    return aplication


app = create_app()



