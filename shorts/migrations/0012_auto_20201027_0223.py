# Generated by Django 2.2.16 on 2020-10-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0011_piece_pending_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='pending_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
