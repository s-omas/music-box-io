from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomForm
from json import dumps
from .load_json import repopulate
import json

# Create your views here.

from .forms import CustomForm



def some_view(request):

    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            for key in form.cleaned_data:
                print(key, form.cleaned_data[key])

            with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/config_dict.json',
                      'w') as outfile:
                json.dump(form.cleaned_data, outfile, indent=4)

            repopulate()

    return render(request, 'form.html', {'form': CustomForm()})

