# Generated by Django 3.0.2 on 2020-03-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200317_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_post',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
