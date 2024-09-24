# from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import ClubFilter, HallFilter, ReviewFilter, TrainingScheduleFilter
# from .models import *
# from .serializer import *
# # Клубы
# class ClubListCreateView(generics.ListCreateAPIView):
#     queryset = Club.objects.all()
#     serializer_class = ClubSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ClubFilter
#
# class ClubRetrieveUpdateDestroyView(generics.RetrieveAPIView):
#     queryset = Club.objects.all()
#     serializer_class = ClubSerializer
#
#
#
# # Залы
# class HallListCreateView(generics.ListCreateAPIView):
#     queryset = Hall.objects.all()
#     serializer_class = HallSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = HallFilter
#
#
# class HallRetrieveUpdateDestroyView(generics.RetrieveAPIView):
#     queryset = Hall.objects.all()
#     serializer_class = HallSerializer
# # Отзывы
# class ReviewListCreateView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ReviewFilter
#
# class ReviewRetrieveUpdateDestroyView(generics.RetrieveAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#
# class TrainingCreateView(generics.ListCreateAPIView):
#     queryset = TrainingSchedule.objects.all()
#     serializer_class = TrainingScheduleSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = TrainingScheduleFilter
#
#
# class TrainingRetrieveUpdateDestroyView(generics.RetrieveAPIView):
#     queryset = TrainingSchedule.objects.all()
#     serializer_class = TrainingScheduleSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Импортируйте нужные разрешения
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sport, Hall, Club, Review, TrainingSchedule  # Импортируйте ваши модели
from .serializers import SportSerializer, HallSerializer, ClubSerializer, ReviewSerializer, TrainingScheduleSerializer  # Импортируйте ваши сериализаторы

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [AllowAny()]
        return super().get_permissions()

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
