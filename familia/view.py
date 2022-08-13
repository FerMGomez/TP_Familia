from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime





def saludo(response):
    return  HttpResponse('HOHOLAHOALHOALHOALHOAL')

def saludando(request):
    return render(request,'template.html',context={})

def familia(request):
    context ={
        'familia':['MARCELA','MIGUEL','RICARDO','FERNANDO','ANALAURA' ],
        
    }
    return render(request,'bandas.html',context=context)

def lista(request):
    context={
        'frutas':['naranja','banana','mandarina','jj'],
    }
    return render(request,'lista.html',context=context)


