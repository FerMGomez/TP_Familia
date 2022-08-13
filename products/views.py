from multiprocessing import context
from django.shortcuts import render
from products.models import Products




def new_date(request):
    new_date = Products.objects.create(
        nombres = 'Ricardo Ramon', 
        apellido = 'Gomez',f_nacimiento = '1980', 
        sexo= 'Masculino', 
        edad = '42')
    context={
        'new_date':new_date
    }
    return render(request,'new_date.html',context=context)

def lista_f(request):
    lista_r = Products.objects.all()
    context={
        'lista_f':lista_r
    }
    return render(request,'lista_f.html',context=context)