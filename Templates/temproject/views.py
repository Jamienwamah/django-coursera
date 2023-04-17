from django.shortcuts import render
from django.http import HttpResponse

def handler404(request, exceptiom):
    return HttpResponse("This 404 no suppose be normal")