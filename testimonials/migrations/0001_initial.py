# Generated by Django 2.2.16 on 2020-10-23 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('author_url', models.URLField()),
                ('book_title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pull_quote', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]