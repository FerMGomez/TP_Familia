from django.contrib import admin
from django.urls import path
from familia.view import saludo, saludando, familia, lista
from products.views import new_date, lista_f

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('saludando/',saludando),
    path('familia/',familia),
    path('lista/',lista),
    path('new-products/',new_date),
    path('lista-f/',lista_f)
]
