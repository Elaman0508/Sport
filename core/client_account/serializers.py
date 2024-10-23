from rest_framework import serializers
from .models import *

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  # Specify fields explicitly


class Payment1Serializer(serializers.ModelSerializer):
    sport_display = serializers.CharField(source='get_sport_display', read_only=True)

    class Meta:
        model = Payment1
        fields = ['id', 'user', 'sport', 'sport_display', 'paid', 'enrollment_date', 'opening_time', 'closing_time', 'is_active']

class SchedulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedul
        fields = ['id', 'circle', 'day_of_week', 'category', 'start_time', 'end_time', 'is_active']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
