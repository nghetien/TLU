# Generated by Django 3.0.2 on 2020-03-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
