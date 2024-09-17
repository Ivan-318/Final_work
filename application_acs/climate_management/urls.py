from django.urls import path
from . import views


urlpatterns = [
    path('', views.climate_management, name="climate_management"),
]
