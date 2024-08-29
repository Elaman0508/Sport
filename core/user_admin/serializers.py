from rest_framework import serializers
from .models import Trainer, Client

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'sport']

class ClientSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)  # Включаем данные тренера

    class Meta:
        model = Client
        fields = ['id', 'name', 'trainer', 'sport', 'payment']
