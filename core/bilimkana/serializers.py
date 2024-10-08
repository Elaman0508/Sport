from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['user', 'basketball_class', 'is_free']

    def validate(self, data):
        user = data['user']
        basketball_class = data['basketball_class']

        # Проверка, является ли пользователь новым (не участвовал ранее)
        if Registration.objects.filter(user=user).exists():
            raise serializers.ValidationError("Вы уже зарегистрированы на занятие или ранее посещали занятия.")

        # Если это первое занятие и оно бесплатное для новых пользователей
        data['is_free'] = basketball_class.is_free_for_new_users
        return data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('author', 'content', 'rating')


class ArenaSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Arena
        fields = (
            'name', 'size', 'flooring', 'court_count', 'equipment', 'type', 'price_per_hour', 'changing_room',
            'lighting',
            'shower', 'reviews')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'rating', 'experience', 'created_at']


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'experience']


class ClassScheduleSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer()

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class ClubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubInfo
        fields = ['title', 'description', 'advantages', 'client_reviews']
