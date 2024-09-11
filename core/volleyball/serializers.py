from rest_framework import serializers
from .models import Hall, Review, HallImage, Circle, CircleImage, TrainingSchedule

class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = ['id', 'image']
        read_only_fields = ['id']
        ref_name = 'VolleyballHallImageSerializer'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'text', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']
        ref_name = 'VolleyballReviewSerializer'

class HallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        fields = [
            'id', 'title', 'description', 'text', 'name', 'dimensions', 'capacity',
            'type', 'covering', 'inventory', 'hourly_rate', 'title1', 'address',
            'phone', 'images', 'reviews'
        ]
        read_only_fields = ['id', 'images', 'reviews']
        ref_name = 'VolleyballHallSerializer'

class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = ['id', 'image']
        read_only_fields = ['id']
        ref_name = 'VolleyballCircleImageSerializer'

class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = [
            'id', 'title', 'description', 'image', 'title1', 'text',
            'description1', 'video_link', 'text1', 'description2',
            'address', 'phone', 'images'
        ]
        read_only_fields = ['id']
        ref_name = 'VolleyballCircleSerializer'

class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = ['id', 'time', 'day', 'sport', 'age_group', 'coach']
        read_only_fields = ['id']
        ref_name = 'VolleyballTrainingSerializer'