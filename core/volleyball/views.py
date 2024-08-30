from rest_framework import generics, filters
from .models import Hall, Review, Circle, TrainingSchedule
from .serializers import HallSerializer, ReviewSerializer, CircleSerializer, TrainingScheduleSerializer

class HallListView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

    def get_queryset(self):
        # Пример фильтрации по названию зала
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(name__icontains=title)
        return queryset

class HallDetailView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        # Пример фильтрации по имени пользователя
        queryset = super().get_queryset()
        user_name = self.request.query_params.get('user_name', None)
        if user_name:
            queryset = queryset.filter(user_name__icontains=user_name)
        return queryset

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CircleListView(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

    def get_queryset(self):
        # Пример фильтрации по названию кружка
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

class CircleDetailView(generics.RetrieveAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class TrainingScheduleListView(generics.ListAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['time', 'day']
    ordering = ['day', 'time']
