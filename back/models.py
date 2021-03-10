from tortoise.models import Model
from tortoise import fields

class Sensor_Bme280(Model):
    class Meta:
        table = "sensor_bme280_values"


    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    humidity = fields.FloatField()
    temperature = fields.FloatField()
    pressure = fields.FloatField()
    altitude = fields.FloatField()
