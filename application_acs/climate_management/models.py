from django.db import models

# Create your models here.


class Temperature(models.Model):
    temperature_value = models.FloatField()
    measurement_time = models.DateTimeField() # время измерения
    unit = models.CharField(max_length=64) # единицы измерения температуры

class Humidity(models.Model): # влажность
    humidity_value = models.FloatField()
    measurement_time = models.DateTimeField()

class Illumination(models.Model): # освещённость
    light_level = models.FloatField()
    measurement_time = models.DateTimeField()

