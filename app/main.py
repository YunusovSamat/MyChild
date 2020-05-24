from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api.routers import router
from app.core.config import DATABASE_URL
from app.core.events import shutdown, startup


def get_application() -> FastAPI:
    application = FastAPI(title="MyChild")

    application.add_event_handler("startup", startup(dsn=DATABASE_URL))
    application.add_event_handler("shutdown", shutdown())

    application.include_router(router)
    application.mount("/gallery", StaticFiles(directory="app/static/gallery"), name="static")

    return application


app = get_application()
