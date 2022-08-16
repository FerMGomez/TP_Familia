from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



def saludo(response):
    return  HttpResponse('HOLA COMO ESTAS?')

def saludando(request):
    return render(request,'template.html',context={})

def bandas(request):
    context ={
        'banda':['MEGADETH','METALLICA','SLAYER'],       
    }
    return render(request,'bandas.html',context=context)

def lista(request):
    context={
        'frutas':['naranja','banana','mandarina','jj'],
    }
    return render(request,'lista.html',context=context)


