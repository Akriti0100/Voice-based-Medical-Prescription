from django.shortcuts import render

# Create your views here.
def voice(request):
    return render(request, 'index.html')
