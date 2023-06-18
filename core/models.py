from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200,default='')
    message=models.CharField(max_length=50000,default='')

    def __str__(self):
        return self.name
