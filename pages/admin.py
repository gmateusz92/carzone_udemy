from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin): #tworzymy klase zeby zrobic tabale w panelu admina
    def thumbnail(self, object): # wstawia zdjecie
        return format_html('<img src="{}" width="40" style="border-radius: 10px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'Photo' # wyswietla fukcje thumbnail jako opis Photo

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name', ) # dzieki temu tworzy link dla id etc. (zeby mozna kliknanac)
    search_fields = ('first_name', 'last_name', 'designation') # tworzy pasek szukania / dokumentacja django
    list_filter = ('designation',) # dodaje filtry z prawej strony


admin.site.register(Team, TeamAdmin)
