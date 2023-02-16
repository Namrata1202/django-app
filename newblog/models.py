from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Blognew(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    dsc = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    likes = models.ManyToManyField(User,related_name='blog_post')
    unlikes = models.ManyToManyField(User,related_name='unlike_post')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Blognew,on_delete=models.CASCADE, related_name="comments")
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.body




