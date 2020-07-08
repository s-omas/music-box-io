from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConfigForm
from django.
# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():

            grid = form.cleaned_data['grid']
            pressure = form.cleaned_data['pressure']

            print(grid, pressure)

    form = ConfigForm
    return render(request, 'form.html', {'form': form})

