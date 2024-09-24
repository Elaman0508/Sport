# filters.py
from django_filters import rest_framework as filters
from .models import *

class HallFilter(filters.FilterSet):
    sport = filters.CharFilter(field_name='sport__name', lookup_expr='icontains')

    class Meta:
        model = Hall
        fields = ['sport']
class ClubFilter(filters.FilterSet):
    sport = filters.CharFilter(field_name='sport__name', lookup_expr='icontains')

    class Meta:
        model = Club
        fields = ['sport']
# Фильтр для отзывов
class ReviewFilter(filters.FilterSet):
    sport = filters.CharFilter(field_name='sport__name', lookup_expr='icontains')

    class Meta:
        model = Review
        fields = ['sport']

# Фильтр для расписания тренировок
class TrainingScheduleFilter(filters.FilterSet):
    sport = filters.CharFilter(field_name='sport__name', lookup_expr='icontains')

    class Meta:
        model = TrainingSchedule
        fields = ['sport']