from django.db import models
from users.models import User

class Chat(models.Model):
    topic = models.CharField(max_length=128, blank=False)
    is_group_chat = models.BooleanField(default=False)
    last_message = models.TextField(blank=False)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(blank = False)
    added_at = models.DateTimeField(blank = False)

class Attachment(models.Model):
   chat =  models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
   url = models.EmailField()
