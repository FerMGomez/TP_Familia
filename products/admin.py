from itertools import product
from django.contrib import admin


from products.models import Products

# Register your models here.

#admin.site.register(Products)
@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['nombres', 'apellido','f_nacimiento' ]