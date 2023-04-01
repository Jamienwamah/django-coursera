from django.shortcuts import render
from django.http import HttpResponse

#Create views here

def handler404(request, exception):
    return HttpResponse('<h1>404: Please exit</h1>')