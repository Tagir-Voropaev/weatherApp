from django.db import models

class default_city(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name
class search_cityModel(models.Model):
    city_name_form = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name_form