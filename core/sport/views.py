from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Импортируйте нужные разрешения
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sport, Hall, Club, Review, TrainingSchedule  # Импортируйте ваши модели
from .serializers import HallSerializer, ClubSerializer, ReviewSerializer, TrainingScheduleSerializer  # Импортируйте ваши сериализаторы

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport']

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [AllowAny()]
        return super().get_permissions()

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport']

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [AllowAny()]
        return super().get_permissions()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport']

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [AllowAny()]
        return super().get_permissions()

class TrainingScheduleViewSet(viewsets.ModelViewSet):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport']

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [AllowAny()]
        return super().get_permissions()
