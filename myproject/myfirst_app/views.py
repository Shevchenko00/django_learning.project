from re import template

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')



def hi(request):
    return render(request, 'hi.html')


def see_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main.html')