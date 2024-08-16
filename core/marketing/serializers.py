from rest_framework import serializers
from .models import Advertisement
from django.conf import settings
from django.conf.urls.static import static


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


