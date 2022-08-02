from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {'cars': paged_cars })

def car_detail(request, id): #wyswietla konkretny wybrany samochod
    single_car = get_object_or_404(Car, pk=id)

    return render(request, 'cars/car_detail.html', {'single_car': single_car})
