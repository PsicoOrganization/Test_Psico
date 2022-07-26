from django.db import models

class TypeSpecialty(models.Model):
    id_type = models.BigAutoField(primary_key=True)
    typeSpecialty = models.CharField('TypeSpecialty', max_length=50)