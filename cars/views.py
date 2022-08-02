from django.shortcuts import render, get_object_or_404
from cars.models import Car

def cars(request):
    return render(request, 'cars/cars.html', {})

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)


    return render(request, 'cars/car_detail.html', {'single_car': single_car})
