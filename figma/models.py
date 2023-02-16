from django.db import models

# Create your models here.
class Country(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    description=models.CharField(max_length=100)

class Clients(models.Model):

    image=models.ImageField(upload_to="img/%y")
    name=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)

def __str__(self):
    return self.title

   

