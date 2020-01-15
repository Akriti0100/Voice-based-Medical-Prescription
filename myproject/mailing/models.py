from django.db import models


class Mails(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=20000)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.email 
