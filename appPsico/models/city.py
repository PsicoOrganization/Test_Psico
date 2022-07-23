from django.db import models
from .psychologist import Psychologist

class City(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Psychologist, related_name='city', on_delete=models.CASCADE)
    city = models.CharField('City', max_length=50)