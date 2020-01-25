from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Medical
from .forms import forms
# Create your views here.
def index(request):
   return render(request,'index.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data['data']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'preview.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms()

    return render(request,'index.html')

