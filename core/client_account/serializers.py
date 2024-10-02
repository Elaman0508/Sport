from rest_framework import serializers
from .models import Schedule, Attendance, Payment1, UserProfile

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  # Specify fields explicitly


class Payment1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment1
        fields = '__all__'  # Specify fields explicitly


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
