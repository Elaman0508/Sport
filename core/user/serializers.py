from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password_confirm', 'first_name', 'last_name', 'phone_number', 'birth_date']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        if CustomUser.objects.filter(phone_number=attrs.get("phone_number")).exists():
            raise serializers.ValidationError("Такой номер уже существует.")

        return attrs

    def create(self, validated_data):
        email = validated_data['email']

        # Проверка уникальности email
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "Пользователь с таким адресом электронной почты уже существует."})

        user = CustomUser.objects.create_user(
            email=email,
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            birth_date=validated_data.get('birth_date')
        )
        return user
