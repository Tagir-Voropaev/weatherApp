# Generated by Django 5.1.3 on 2024-11-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_search_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='search_City',
        ),
    ]
