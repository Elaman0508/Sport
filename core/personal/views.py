from rest_framework import viewsets
from .models import Schedule, Attendance, Payment1
from .serializers import ScheduleSerializer, AttendanceSerializer, Payment1Serializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class Payment1ViewSet(viewsets.ModelViewSet):
    queryset = Payment1.objects.all()
    serializer_class = Payment1Serializer
