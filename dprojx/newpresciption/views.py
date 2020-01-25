from django.shortcuts import render
from dprojx.dappx.NLP import nlp

# Create your views here.
def newpre(request):
    return render(request, 'newprescription.html', {})
def new(request):
    data = nlp('patients name is saraj sharma  He is 25  years old and date of birth is 28th february 1999 he is suffering from acute bronchitis He is having symptoms which are dry cough for the last 3 days no fever and running nose he needs to take the following medicines  azithromycin 500 mg once a day for 3 days and robitussin 5 ml thrice a day for 5 days he is advised to drink warm water and he is not allowed to eat grapes')
    context ={
        'data' : data
    }
    return render(request,'record.html',context)
def record(request):
    return render()