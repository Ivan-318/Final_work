from django.shortcuts import render


def climate_management(request):
    return render(request, "climate_management/climate_management.html")
