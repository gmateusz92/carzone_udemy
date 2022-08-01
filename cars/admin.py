from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')# wyswietla tebele
    list_display_links = ('id', 'thumbnail', 'car_title')  # dzieki temu tworzy link dla id etc. (zeby mozna kliknanac)
    list_editable = ('is_featured', ) #mozna edytowac z prawej strony
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style')  # tworzy pasek szukania / dokumentacja django
    list_filter = ('city', 'model', 'body_style', 'fuel_type')  # dodaje filtry z prawej strony
    def thumbnail(self, object): # wstawia zdjecie
        return format_html('<img src="{}" width="40" style="border-radius: 10px;"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image' # wyswietla fukcje thumbnail jako opis Photo

admin.site.register(Car, CarAdmin)
