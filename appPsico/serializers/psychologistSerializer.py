from rest_framework import serializers
from appPsico.models.psychologist import Psychologist
from appPsico.models.account import Account
from appPsico.models.city import City
from appPsico.models.type_speacialty import TypeSpecialty

from appPsico.serializers.accountSerializer import AccountSerializer
from appPsico.serializers.citySerializer import CitySerializer
from appPsico.serializers.type_speacialtySerializer import TypeSpecialtySerializer

class PsychologistSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    city = CitySerializer()
    typeSpecialty = TypeSpecialtySerializer()
    class Meta:
        model = Psychologist
        fields = ['id', 'username', 'password', 'name', 'email', 'city', 'identification', 'address', 'phone', 'typeSpecialty', 'description', 'gender', 'price', 'account']

    def create(self, validated_data):
        cityData = validated_data.pop('city')
        typeSpecialtyData = validated_data.pop('typeSpecialty')
        accountData = validated_data.pop('account')

        cityInstance = City.objects.create(**cityData)
        typeSpecialtyInstance = TypeSpecialty.objects.create(**typeSpecialtyData)

        psychologistInstance = Psychologist.objects.create(city=cityInstance,type=typeSpecialtyInstance,**validated_data)
        Account.objects.create(user=psychologistInstance, **accountData)
        return psychologistInstance
    


    def to_representation(self, obj):
        psychologist = Psychologist.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        typeSpecialty = TypeSpecialty.objects.get(psychologist.typeSpecialty)
        city = City.objects.get(psychologist.city)
        return {
            'id': psychologist.id,
            'username': psychologist.username,
            'password': psychologist.password,
            'name': psychologist.name,
            'email': psychologist.email,
            'city': {
                'id_city': city.id,
                'city': city.city
            },
            'identification': psychologist.identification,
            'address': psychologist.address,
            'phone': psychologist.phone,
            'typeSpecialty': {
                'id_typeSpecialty': typeSpecialty.id,
                'typeSpecialty': typeSpecialty.typeSpecialty
            },
            'description': psychologist.description,
            'gender': psychologist.gender,
            'price': psychologist.price,
            'account':{
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
            }
        }
