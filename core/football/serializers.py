from rest_framework import serializers
from .models import Hall, Review, HallImage, TrainingSchedule, Circle, CircleImage


class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = ['id', 'image']

class HallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True, read_only=True)  # Включаем изображения в сериализатор
    reviews = serializers.StringRelatedField(many=True, read_only=True)  # Включаем отзывы в сериализатор

    class Meta:
        model = Hall
        fields = ['id', 'title', 'description', 'text', 'name', 'dimensions', 'capacity', 'type', 'covering', 'inventory', 'hourly_rate', 'title1', 'address', 'phone', 'images', 'reviews']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'text', 'rating', 'created_at']
class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = ['image']

class CircleSerializer(serializers.ModelSerializer):
    images = CircleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Circle
        fields = [
            'title', 'description', 'image',
            'title1', 'text', 'description1', 'video_link',
            'text1', 'description2',
            'address', 'phone',
            'images'
        ]

class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = ['time', 'day', 'sport', 'age_group', 'coach']
