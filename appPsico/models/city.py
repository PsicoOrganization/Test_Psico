from django.db import models

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    city = models.CharField('City', max_length=50)