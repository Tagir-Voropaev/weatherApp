# Generated by Django 5.1.3 on 2024-11-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_delete_city_delete_search_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='default_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
