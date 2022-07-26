from dataclasses import field
from rest_framework import serializers
from appPsico.models.psychologist import Psychologist
from appPsico.models.city import City
from appPsico.models.type_speacialty import TypeSpecialty

from appPsico.serializers.citySerializer import CitySerializer
from appPsico.serializers.type_speacialtySerializer import TypeSpecialtySerializer

class PsychologistSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    typeSpecialty = TypeSpecialtySerializer()
    class Meta:
        model = Psychologist
        fields = '__all__'
        #fields = ['id', 'username', 'password', 'name', 'email', 'city', 'identification', 'address', 'phone', 'typeSpecialty', 'description', 'gender', 'price', 'lastChangeDate']

    def create(self, validated_data):
        cityData = validated_data.pop('city')
        typeSpecialtyData = validated_data.pop('typeSpecialty')
        cityInstance = City.objects.create(**cityData)
        typeSpecialtyInstance = TypeSpecialty.objects.create(**typeSpecialtyData)
        psychologistInstance = Psychologist.objects.create(city=cityInstance,typeSpecialty=typeSpecialtyInstance,**validated_data)
        
        return psychologistInstance

    def to_representation(self, obj):
        psychologist = Psychologist.objects.get(id=obj.id)
        typeSpecialty = TypeSpecialty.objects.get(psychologist.typeSpecialty)
        city = City.objects.get(psychologist.city)
        return {
            'id': psychologist.id,
            'username': psychologist.username,
            'password': psychologist.password,
            'name': psychologist.name,
            'email': psychologist.email,
            'city': {
                'id_city': city.id_city,
                'name_city': city.name_city
            },
            'identification': psychologist.identification,
            'address': psychologist.address,
            'phone': psychologist.phone,
            'typeSpecialty': {
                'id_typeSpecialty': typeSpecialty.id_typeSpecialty,
                'name_type': typeSpecialty.name_type
            },
            'description': psychologist.description,
            'gender': psychologist.gender,
            'price': psychologist.price,
            'lastChangeDate': psychologist.lastChangeDate,
        }
    

