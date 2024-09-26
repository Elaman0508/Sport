from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = '__all__'
        ref_name = 'HallImageSerializer'  # Add ref_name # Add ref_name


class HallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        fields = '__all__'
        ref_name = 'HallSerializer'  # Add ref_name


class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = '__all__'
        ref_name = 'CircleImageSerializer'  # Add ref_name


class CircleSerializer(serializers.ModelSerializer):
    circle_images = CircleImageSerializer(many=True, read_only=True)

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


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'sport']  # Include the fields you want to expose

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
