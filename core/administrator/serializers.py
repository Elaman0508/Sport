from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = '__all__'
        ref_name = 'HallImageSerializer'  # Добавлено ref_name

class HallSerializer(serializers.ModelSerializer):
    hall_images = HallImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        fields = '__all__'
        ref_name = 'HallSerializer'  # Задайте уникальное имя

class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'

class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = '__all__'
        ref_name = 'CircleImageSerializer'  # Add ref_name

#Кружки
class CircleSerializer(serializers.ModelSerializer):
    circle_images = CircleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Circle
        fields = '__all__'
        ref_name = 'CircleSerializer'

class SchedulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedul
        fields = '__all__'
#login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        ref_name = 'UserLoginSerializer'  # Add ref_name here

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Неверный логин или пароль.")
        return {'user': user}

#Тренеры
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
#Клиенты
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'trainer', 'sport', 'payment_method']  # Include the fields you want to expose

    # Optional: Customize the representation to include the trainer's name
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['trainer'] = {
            'id': instance.trainer.id,
            'name': f"{instance.trainer.first_name} {instance.trainer.last_name}",
        }
        return representation
#реклама
class AdvertisementSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)  # Убедитесь, что поле правильно объявлено
    class Meta:
        model = Advertisement
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'comment', 'created_at', 'rating']
        ref_name = 'SportReviewSerializer'  # Уникальное имя для Swagger

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'name', 'sport', 'monthly_price', 'created_at']  # Убедитесь, что поле создано
        read_only_fields = ['created_at']
