# Generated by Django 2.2.16 on 2021-08-09 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]
