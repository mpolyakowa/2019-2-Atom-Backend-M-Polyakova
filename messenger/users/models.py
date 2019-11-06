from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    nick = models.CharField(max_length=128, blank = False)
    avatar = models.EmailField()

class Member(models.Model):
    chat =  models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True) 
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_read_message = models.ForeignKey('chats.Message', on_delete=models.SET_NULL, null=True)
       
