from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {'cars': paged_cars })

def car_detail(request, id): #wyswietla konkretny wybrany samochod
    single_car = get_object_or_404(Car, pk=id)

    return render(request, 'cars/car_detail.html', {'single_car': single_car})

def search(request):
    cars = Car.objects.order_by('-created_date')  # latest cars na stronie

    if 'keyword' in request.GET: #jezeli wpiszemy w search jakis keyword
        keyword = request.GET['keyword']# przechowujemy keyword w tej zmiennej keyword
        if keyword: #sprawdzam czy keyword nie jest puste
            cars = cars.filter(Q(description__icontains=keyword) | Q(car_title__icontains=keyword)) #icointains szuka wszedzie takie klucza liter

        return render(request, 'cars/search.html', {'cars': cars, })


