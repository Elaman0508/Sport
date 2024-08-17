from rest_framework import serializers
from .models import Advertisement, Tariff, Payment
from django.conf import settings
from django.conf.urls.static import static


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class AdvertisementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'photo', 'description']


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['id', 'name', 'price', 'duration_days']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'card_holder_name', 'card_number', 'expiry_date', 'cvc', 'amount', 'created_at']
