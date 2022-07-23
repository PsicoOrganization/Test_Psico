from django.db import models

class TypeSpecialty(models.Model):
    id = models.AutoField(primary_key=True)
    typeSpecialty = models.CharField('TypeSpecialty', max_length=50)