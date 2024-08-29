from rest_framework import serializers
from .models import *


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
