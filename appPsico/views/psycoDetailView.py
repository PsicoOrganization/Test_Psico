from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from appPsico.models.psychologist import Psychologist
from appPsico.serializers.psychologistSerializer import PsychologistSerializer

class PsycoDetailView(generics.RetrieveAPIView):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tockendBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tockendBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse,status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)