# dappx/views.py
from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import MyForm,NameForm
from .NLP import nlp
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from .emailsend import send
from dprojx.settings import EMAIL_HOST_USER
def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def responseform(request):
    form = MyForm()
    return render(request, 'responseform.html', {'form': form});
# Add prescription
def newpre(request):
    return render(request, 'newprescription.html', {})
def record(request):
    return render(request,'startrecord.html',{})
def new(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form = form.cleaned_data['text'],
            data = nlp(form)
            context ={
                'data': data
            }
            return render(request, 'record.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm(request.POST)

    return render(request,'startrecord.html')

def sendmail(request):
    send()
    return render(request, 'sendmail.html', {})

