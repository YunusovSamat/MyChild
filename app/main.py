from fastapi import FastAPI

from app.api.routers import router
from app.core.config import DATABASE_URL
from app.core.events import shutdown
from app.core.events import startup


def get_application() -> FastAPI:
    application = FastAPI(title="MyChild")

    application.add_event_handler("startup", startup(dsn=DATABASE_URL))
    application.add_event_handler("shutdown", shutdown())

    application.include_router(router)

    return application


app = get_application()
