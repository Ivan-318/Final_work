from django.contrib import admin
from . import models

# Register your models here.

class IlluminationAdmin(admin.ModelAdmin):
    list_display = ('measurement_time', )

class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('measurement_time', )

class HumidityAdmin(admin.ModelAdmin):
    list_display = ('measurement_time', )

admin.site.register(models.Illumination, IlluminationAdmin)
admin.site.register(models.Temperature, TemperatureAdmin)
admin.site.register(models.Humidity, HumidityAdmin)