from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .city import City
from .type_speacialty import TypeSpecialty


class PsychologistManager(BaseUserManager):
    def create_psychologist(self, username, password=None):
        """
        Creates and saves a Psychologist with the given username and
        """
        if not username:
            raise ValueError('Psychologist must have an username')
        psychologist = self.model(username=username)
        psychologist.set_password(password)
        psychologist.save(using=self._db)
        return psychologist

    def create_superpsychologist(self, username, password):
        """
        Creates and saves a superpsychologist with the given username and password.
        """
        psychologist = self.create_psychologist(
            username=username,
            password=password,
        )
        psychologist.is_admin = True
        psychologist.save(using=self._db)
        return psychologist

class Psychologist(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=15, unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('Name',max_length=30)
    email = models.EmailField('Email',max_length=100)
    city = models.ForeignKey(City, related_name='City', on_delete=models.CASCADE)
    identification = models.CharField('Identification',max_length=20)
    address = models.CharField('Address',max_length=60,blank=True,default='')
    phone = models.CharField('Phone',max_length=10)
    typeSpecialty = models.ForeignKey(TypeSpecialty, related_name='TypeSpecialty', on_delete=models.CASCADE)
    description = models.CharField('Description',max_length=500,blank=True,default='')
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )  #Dominio del genero
    gender = models.CharField('Gender',max_length=1,choices=GENDER)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    lastChangeDate = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = PsychologistManager()
    USERNAME_FIELD = 'username'
