from appPsico.models.type_speacialty import TypeSpecialty
from rest_framework import serializers
class TypeSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSpecialty
        fields = ['typeSpecialty']