from databases import DatabaseURL
from starlette.config import Config

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
SQL_DEBUG = config("SQL_DEBUG", cast=bool, default=False)
DATABASE_URL = config("DB_CONNECTION", cast=DatabaseURL)
