from django.contrib import admin
from django.urls import path
from .view import bandas
from familia.view import saludo, saludando,lista, bandas
from products.views import new_date, lista_f

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('saludando/',saludando),
    path('lista/',lista),
    path('new-products/',new_date),
    path('lista-f/',lista_f),
    path('bandas/', bandas)
]
