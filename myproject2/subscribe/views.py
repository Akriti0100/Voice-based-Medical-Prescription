from django.shortcuts import render
from django.conf import settings
from myproject2.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
# Create your views here.
#DataFlair #Send Email
msg2 = EmailMessage()

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        msg = EmailMultiAlternatives(subject,message,EMAIL_HOST_USER,[recepient])
        msg.attach_alternative('/images/Ayush.jpg', "image/jpg")
        msg.send()
        #send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form': sub})
