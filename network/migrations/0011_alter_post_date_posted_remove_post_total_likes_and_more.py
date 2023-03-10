# Generated by Django 4.0.4 on 2022-12-18 09:50

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_post_total_likes_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 9, 50, 11, 769585, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='post',
            name='total_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='total_likes',
            field=models.ManyToManyField(related_name='total_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
