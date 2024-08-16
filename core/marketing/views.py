from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django.conf import settings
from rest_framework import viewsets


class AdvertisementListCreateView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


# Retrieve, update, or delete a specific advertisement
# class AdvertisementDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
