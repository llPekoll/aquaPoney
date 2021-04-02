import os

from pydantic import BaseModel
from fastapi import Security, Depends, FastAPI, HTTPException, Body, Request, APIRouter
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_403_FORBIDDEN
from tortoise.contrib.fastapi import register_tortoise

import endpoints


API_KEY_NAME = os.environ.get("API_KEY_NAME")
API_KEY = os.environ.get("API_KEY")

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Not this time!!! You need a proper API Key",
        )


user = os.environ.get("PSQL_USER")
password = os.environ.get("PSQL_PASSWORD")

port = os.environ.get("PSQL_PORT")
db = os.environ.get("PSQL_DATABASE")
host = os.environ.get("PSQL_HOST")
server = f"{host}:{port}"
url = f"postgres://{user}:{password}@{server}/{db}"

register_tortoise(
    app,
    db_url=url,
    modules={"models": ["back.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


app.mount("/static", StaticFiles(directory="/front/public/"), name="static")


api_router = APIRouter()


api_router.include_router(endpoints.router, prefix="", tags=["Basic Feature"])
