from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()  # value list flat=True zwraca liste a nie slownik
    year_search = Car.objects.values_list('year', flat=True).distinct()  # distinct() zapobiega pobieraniu takich samych wierszy z bazy danych
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search,
            'cars': paged_cars
            }

    return render(request, 'cars/cars.html', data)

def car_detail(request, id): #wyswietla konkretny wybrany samochod
    single_car = get_object_or_404(Car, pk=id)

    return render(request, 'cars/car_detail.html', {'single_car': single_car})

def search(request):
    cars = Car.objects.order_by('-created_date')  # latest cars na stronie

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()              #sa 3 wyszukiwarki to dodajemy do template cars search
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET: #jezeli wpiszemy w search jakis keyword to
        keyword = request.GET['keyword']# przechowujemy keyword w tej zmiennej keyword
        if keyword: #sprawdzam czy keyword nie jest puste
            cars = cars.filter(Q(description__icontains=keyword) | Q(car_title__icontains=keyword)) #icointains szuka wszedzie takie klucza liter

    if 'model' in request.GET:
        model = request.GET['model']  # ['model'] jest uzyte w template home w wyszukiwarce
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']  # ['city'] jest uzyte w template home w wyszukiwarce
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']  # ['year'] jest uzyte w template home w wyszukiwarce
        if year:  # sprawdzam czy keyword nie jest puste
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']  # ['body_style'] jest uzyte w template home w wyszukiwarce
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

        data = {
                'cars': cars,
                'model_search': model_search,
                'city_search': city_search,
                'year_search': year_search,
                'body_style_search': body_style_search,
                'transmission_search': transmission_search,
                }

    return render(request, 'cars/search.html', data)


