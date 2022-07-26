from django.db import models

class TypeSpecialty(models.Model):
    id_type = models.AutoField(primary_key=True)
    name_type = models.CharField('TypeSpecialty', max_length=50)