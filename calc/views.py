from django.http import HttpResponse
from django.shortcuts import render


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    return render(request, 'home.html')