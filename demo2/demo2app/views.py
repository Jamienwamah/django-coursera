from django.shortcuts import render
from django.http import HttpResponse
from demo2app.forms import ReservationForm

# Create your views here.

def reserve_view(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.valid():
            form.save
    context = {'form': form}
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse("This is an about page")
