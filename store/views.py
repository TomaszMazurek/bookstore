from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'template.html')


def store(request):
    return render(request, 'store.html')
