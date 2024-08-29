from rest_framework import generics
from .models import SportClass
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class SportClassListCreateView(generics.ListCreateAPIView):
    queryset = SportClass.objects.all()
    serializer_class = SportClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport_type', 'schedule']


class SportClassRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportClass.objects.all()
    serializer_class = SportClassSerializer
