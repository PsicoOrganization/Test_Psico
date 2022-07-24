from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from appPsico.models.psychologist import Psychologist
from appPsico.serializers.psychologistSerializer import PsychologistSerializer

class PsycoListView(generics.RetrieveAPIView):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes = (IsAuthenticated,)

# To do... Mostrar la lista de los psicologos