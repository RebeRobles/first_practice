from django.http.response import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    return redirect('/')

def show(request, my_val):
    return HttpResponse(f'placeholder para mostar el blog número: {my_val}')

def edit(request, my_val):
    return HttpResponse(f'placeholder para editar el blog número: {my_val}')

def destroy(request, my_val):
    return redirect('/blogs')

def json(request): 
    return JsonResponse({'Titulo': 'placeholder para mostrar un Json',
    'nombre': 'Rebecca',
    'curso': 'Curso 0071 Python'})