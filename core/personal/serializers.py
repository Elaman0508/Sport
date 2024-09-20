from rest_framework import serializers
from .models import Schedule, Attendance, Payment1, UserProfile


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class Payment1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment1
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'phone', 'birth_date', 'gender', 'address']