from rest_framework import viewsets
from .models import Schedule, Attendance, Payment1, UserProfile
from .serializers import ScheduleSerializer, AttendanceSerializer, Payment1Serializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment1.objects.all()
    serializer_class = Payment1Serializer



class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]