# Generated by Django 2.2.16 on 2020-10-28 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0012_auto_20201027_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug_field',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
