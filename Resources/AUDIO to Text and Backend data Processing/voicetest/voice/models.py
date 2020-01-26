from django.db import models

# Create your models here.
class Medical(models.Model):
    prescriptions = models.TextField(max_length=1000)
