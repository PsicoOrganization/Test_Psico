from django.db import models
from .psychologist import Psychologist

class TypeSpecialty(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Psychologist, related_name='typeSpecialty', on_delete=models.CASCADE)
    TypeSpecialty = models.CharField('TypeSpecialty', max_length=50)