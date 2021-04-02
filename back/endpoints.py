from random import randint
from datetime import datetime

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from tortoise.contrib.pydantic import pydantic_model_creator

from back.models import Sensor_Bme280


router = APIRouter()

templates = Jinja2Templates(directory="/front/public/")
RAND_VALUE = randint(1, 303423424234)


@app.get("/heath")
def heath(api_key: APIKey = Depends(get_api_key)):
    return {"status": "ok"}


@app.get("/")
def heath(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "rand_val": RAND_VALUE,},
    )


@app.get("/sensor/{sensor}")
async def get_sensor_values(sensor: str):
    if sensor == "all":
        return "all_sensor"
    if sensor == "bme280":
        allof = []
        sens = await Sensor_Bme280.all()
        for sen in sens:
            bme280_Pydantic = pydantic_model_creator(Sensor_Bme280)
            tourpy = await bme280_Pydantic.from_tortoise_orm(sen)
            tourpy = tourpy.dict()
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
    bme280: Bm280Values = Body(...), api_key: APIKey = Depends(get_api_key)
):
    jose = {**bme280.dict()}
    await Sensor_Bme280.create(**bme280.dict(), date=datetime.now())
    allof = []
    sens = await Sensor_Bme280.all()
    return {"sucess": True}
