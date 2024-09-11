from rest_framework import generics
from .models import Trainer, Client
from .serializers import TrainerSerializer, ClientSerializer

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
