from django.db import models
from django.conf import settings

# Create your models here.
from django.db import models



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    

    def __str__(self):
        return self.title

