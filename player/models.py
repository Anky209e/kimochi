from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=10,default="")

    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='songs',null=True)
    cover = models.FileField(upload_to='covers',null=True)

    def __str__(self):
        return "-".join([self.name,self.artist])


