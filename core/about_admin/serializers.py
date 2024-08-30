from rest_framework import serializers
from .models import Hall, HallImage, Schedule, CircleImage, Circle


class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallImage
        fields = ['id', 'image']
        ref_name = 'AboutAdminHallImageSerializer'

class HallSerializer(serializers.ModelSerializer):
    images = HallImageSerializer(many=True, read_only=True)  # Включаем изображения зала
    class Meta:
        model = Hall
        fields = [
            'id', 'title', 'phone', 'address', 'description', 'sports',
             'size', 'quantity', 'hall_type', 'coverage',
            'inventory', 'hourly_rate', 'dressing_room',
            'lighting', 'shower', 'images'
        ]
        ref_name = 'AboutAdminourHallSSerializer'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'hall', 'day_of_week', 'start_time', 'end_time']
        ref_name = 'AboutAdminourScheduleSerializer'
class CircleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleImage
        fields = ['id', 'image']
        ref_name = 'AboutAdminCircleImageSerializer'  # Уникальное имя для Swagger

class CircleSerializer(serializers.ModelSerializer):
    images = CircleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Circle
        fields = [
            'id', 'title', 'phone', 'address', 'sports', 'images',
            'header1', 'description1',
            'header2', 'description2',
            'header3', 'description3',
            'header4', 'description4'
        ]
        ref_name = 'AboutAdminCircleSerializer'