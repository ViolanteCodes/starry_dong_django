# Generated by Django 2.2.16 on 2020-10-25 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='published_date',
        ),
    ]
