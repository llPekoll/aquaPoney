from random import randint
import os
from fastapi import Security, Depends, FastAPI, HTTPException, Body, Request
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel

from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from back.models import Sensor_Bme280
from datetime import datetime



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

templates = Jinja2Templates(directory="/front/public/")
app.mount("/static", StaticFiles(directory="/front/public/"), name="static")
rand_value = randint(1, 303423424234)

@app.get("/")
def heath(request: Request):
        return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "rand_val": rand_value,
        },
    )

@app.get("/heath")
def heath(api_key: APIKey = Depends(get_api_key)):
    return {"status":"ok"}


@app.get("/sensor/{sensor}")
async def get_sensor_values(sensor:str):
    if sensor == "all":
        return "all_sensor"
    if sensor == "bme280":
        allof = []
        sens = await Sensor_Bme280.all()
        for sen in sens: 
            bme280_Pydantic = pydantic_model_creator(Sensor_Bme280)
            tourpy = await bme280_Pydantic.from_tortoise_orm(sen)
            tourpy= tourpy.dict()
            del tourpy["id"]
            allof.append(tourpy)
        return allof


class Bm280Values(BaseModel):
    humidity: float = None
    temperature: float = None
    pressure: float = None
    altitude: float = None

@app.post("/bme280")
async def post_sensor_values(
    bme280: Bm280Values = Body(...),
    api_key: APIKey = Depends(get_api_key)):
    jose = {**bme280.dict()}
    await Sensor_Bme280.create(**bme280.dict(), date=datetime.now())
    allof = []
    sens = await Sensor_Bme280.all()
    return {"sucess":True}
