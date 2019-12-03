from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    nick = models.CharField(verbose_name='Никнейм', max_length=128, blank = False)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='images', null=True)
    contacts = ArrayField(models.IntegerField(blank = True, null=True), blank = True, null=True, verbose_name="Массив id контактов пользователя")
    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Member(models.Model):
    chat =  models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True, verbose_name="Идентификатор чата") 
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Идентификатор пользователя")
    last_read_message = models.ForeignKey('chats.Message', on_delete=models.SET_NULL, null=True, verbose_name="Идентификатор последнего прочитанного сообщения")
    class Meta:
        ordering = ['id']
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
