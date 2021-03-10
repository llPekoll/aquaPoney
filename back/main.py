import os
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

from tortoise.contrib.fastapi import register_tortoise
from back.models import Sensor_Bme280


API_KEY = "yo"
API_KEY_NAME = "hann"


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
            status_code=HTTP_403_FORBIDDEN, detail="Not this time!!! You need a proper API Key"
        )

@app.get("/")
def heath(api_key: APIKey = Depends(get_api_key)):
    return "mdgr"



user = os.environ.get("PSQL_USER")
password =os.environ.get("PSQL_PASSWORD")

port =os.environ.get("PSQL_PORT")
db =os.environ.get("PSQL_DATABASE")
host =os.environ.get("PSQL_HOST")
server = f"{host}:{port}"
url = f"postgres://{user}:{password}@{server}/{db}"


register_tortoise(
    app,
    db_url=url,
    modules={"models": ["back.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
