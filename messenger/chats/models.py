from django.db import models
# from users.models import User

class Chat(models.Model):
    topic = models.CharField(verbose_name='название', max_length=128, blank=False)
    is_group_chat = models.BooleanField(verbose_name='Это групповой чат?', default=False)
    last_message = models.IntegerField(verbose_name='Id последнего сообщения', null=False)
    class Meta:
        ordering = ['id']
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

# class Message(models.Model):
#     chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Идентификатор чата',)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Идентификатор пользователя',)
#     content = models.TextField(blank = False, verbose_name='Текст сообщения')
#     added_at = models.DateTimeField(verbose_name='Время добавления сообщения', blank = False)
#     class Meta:
#         ordering = ['id']
#         verbose_name = 'Сообщение'
#         verbose_name_plural = 'Сообщения'

# class Attachment(models.Model):
#    chat =  models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Идентификатор чата')
#    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Идентификатор пользователя')
#    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, verbose_name='Идентификатор сообщения')
#    url = models.EmailField(verbose_name='Ссылка')
#    class Meta:
#         ordering = ['id']
#         verbose_name = 'Документ'
#         verbose_name_plural = 'Документы'
