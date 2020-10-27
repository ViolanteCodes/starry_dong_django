# Generated by Django 2.2.16 on 2020-10-27 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0010_piece_audio_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='pending_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]