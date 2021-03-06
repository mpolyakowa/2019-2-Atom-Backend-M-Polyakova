# Generated by Django 2.2.5 on 2019-11-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128, verbose_name='название')),
                ('is_group_chat', models.BooleanField(default=False, verbose_name='Это групповой чат?')),
                ('last_message', models.IntegerField(verbose_name='Id последнего сообщения')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
                'ordering': ['id'],
            },
        ),
    ]
