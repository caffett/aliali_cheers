from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    discription = models.TextField(max_length=4096, null=True)
    avatar = models.ImageField(upload_to='user/avatars', default="avatars/default.jpg")
    face1 = models.ImageField(upload_to="user/faces/", null=True, blank=True)
    face2 = models.ImageField(upload_to="user/faces/", null=True, blank=True)
    face3 = models.ImageField(upload_to="user/faces/", null=True, blank=True)
    face4 = models.ImageField(upload_to="user/faces/", null=True, blank=True)
    face5 = models.ImageField(upload_to="user/faces/", null=True, blank=True)

    def __unicode__(self):
        return self.username


