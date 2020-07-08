from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomForm

# Create your views here.

from .forms import CustomForm

def some_view(request):
    return render(request, 'form.html', {'form': CustomForm()})
