# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
def __str__(self):
    return self.user.username

Gender_Choices=(
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
)

class Menu(models.Model):
      Name  = models.CharField(max_length=100)
      Age = models.CharField(max_length=100)
      Gender = Gender_Choices


