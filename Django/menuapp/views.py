from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to home</h1>')
def about(request):
    return HttpResponse('<h1>This is About page</h1>')
def menu(request):
    return HttpResponse('<h1>What would you love to be offered<h1>')
