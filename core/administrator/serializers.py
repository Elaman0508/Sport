from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'
        ref_name = 'HallSerializer'
    def validate(self, attrs):
        if 'image' not in attrs or attrs['image'] is None:
            attrs['image'] = self.instance.image  # Эски сүрөттү колдонуу
        # Ушул сыяктуу башка атрибуттарды текшерүү
        return super().validate(attrs)

class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'
#Кружки
class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'  # Же конкреттүү талааларды тандап алсаңыз болот
        ref_name = 'CircleSerializer'

    def create(self, validated_data):
        # Circle моделинин жаңы экземплярын түзүү
        return Circle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Circle моделинин экземплярын жаңыртуу
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

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
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'image', 'sport']

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
    class Meta:
        model = Advertisement
        fields = '__all__'

    def update(self, instance, validated_data):
        # Эгер файл жаңы жүктөлбөсө, мурунку файлды сактап калуу
        file = validated_data.get('file', None)
        if not file and instance.file:
            validated_data['file'] = instance.file

        # Башка талааларды да текшерип, мурунку маалыматтарды сактап калуу
        title = validated_data.get('title', None)
        if not title:
            validated_data['title'] = instance.title

        title1 = validated_data.get('title1', None)
        if not title1:
            validated_data['title1'] = instance.title1

        title2 = validated_data.get('title2', None)
        if not title2:
            validated_data['title2'] = instance.title2

        title3 = validated_data.get('title3', None)
        if not title3:
            validated_data['title3'] = instance.title3

        description = validated_data.get('description', None)
        if not description:
            validated_data['description'] = instance.description

        phone = validated_data.get('phone', None)
        if not phone:
            validated_data['phone'] = instance.phone

        address = validated_data.get('address', None)
        if not address:
            validated_data['address'] = instance.address

        site_name = validated_data.get('site_name', None)
        if not site_name:
            validated_data['site_name'] = instance.site_name

        site_link = validated_data.get('site_link', None)
        if not site_link:
            validated_data['site_link'] = instance.site_link

        installment_plan = validated_data.get('installment_plan', None)
        if not installment_plan:
            validated_data['installment_plan'] = instance.installment_plan

        return super().update(instance, validated_data)

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
