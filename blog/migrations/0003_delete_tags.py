# Generated by Django 2.2.16 on 2020-10-26 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tags',
        ),
    ]