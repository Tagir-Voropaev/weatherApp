# Generated by Django 5.1.3 on 2024-11-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_default_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='default_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('feels_like', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('temp', models.IntegerField()),
                ('temp_min', models.IntegerField()),
                ('temp_max', models.IntegerField()),
            ],
        ),
    ]