from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import HallImage, Schedule, Hall, CircleImage, Schedul, Circle


class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = '__all__'
        ref_name = 'HallImageSerializer'  # Add ref_name


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        ref_name = 'ScheduleSerializer'  # Add ref_name


class HallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True, read_only=True)
    schedule = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        fields = '__all__'
        ref_name = 'HallSerializer'  # Add ref_name


class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = '__all__'
        ref_name = 'CircleImageSerializer'  # Add ref_name


class SchedulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedul
        fields = '__all__'
        ref_name = 'SchedulSerializer'  # Add ref_name


class CircleSerializer(serializers.ModelSerializer):
    circle_images = CircleImageSerializer(many=True, read_only=True)
    schedul = SchedulSerializer(many=True, read_only=True)

    class Meta:
        model = Circle
        fields = '__all__'
        ref_name = 'CircleSerializer'  # Add ref_name
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