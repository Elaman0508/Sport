from rest_framework import generics
from .models import Hall, Review, Circle, TrainingSchedule
from .serializers import HallSerializer, ReviewSerializer, CircleSerializer, TrainingScheduleSerializer
from rest_framework import filters
class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class HallDetailView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CircleListView(generics.ListAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class CircleDetailView(generics.RetrieveAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class TrainingScheduleListView(generics.ListAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['time', 'day']
    ordering = ['day', 'time']
