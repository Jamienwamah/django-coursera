from django.shortcuts import render
from django.http import HttpResponse
from demoapp.forms import InputForm

# Create your views here.

def form_view(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)
