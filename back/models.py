from tortoise.models import Model
from tortoise import fields

class Sensor_Bme280(Model):
    class Meta:
        table = "bme280_values"

    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    humidity = fields.FloatField()
    temperature = fields.FloatField()
    pressure = fields.FloatField()
    altitude = fields.FloatField()

class Maree(Model):
    class Meta:
        table = "marees"

    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    pump_state = fields.BooleanField()

class WaterLevel(Model):
    class Meta:
        table = "waterlevels"

    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    water_level = fields.IntField()


class Ph(Model):
    class Meta:
        table = "Phs"

    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    ph = fields.IntField()
    temperature = fields.IntField()
