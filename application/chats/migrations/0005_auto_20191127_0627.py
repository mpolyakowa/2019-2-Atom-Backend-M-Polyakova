# Generated by Django 2.2.5 on 2019-11-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20191127_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.IntegerField(null=True, verbose_name='Id последнего сообщения'),
        ),
    ]
