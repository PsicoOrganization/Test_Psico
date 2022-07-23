from django.contrib import admin
from .models.psychologist import Psychologist
from .models.account import Account
from .models.city import City
from .models.type_speacialty import TypeSpecialty

admin.site.register(Psychologist)
admin.site.register(Account)
admin.site.register(City)
admin.site.register(TypeSpecialty)
