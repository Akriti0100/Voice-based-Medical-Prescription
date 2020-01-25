# dappx/forms.py
from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')


class MyForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=100)
    email = forms.EmailField(label='Enter your email', max_length=100)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
