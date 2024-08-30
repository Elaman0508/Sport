from time import timezone
from django.db.models import Q
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Hall, Schedule, Circle
from .serializers import HallSerializer, ScheduleSerializer, CircleSerializer


class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = (MultiPartParser, FormParser)  # Поддержка загрузки файлов

class HallRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = (MultiPartParser, FormParser)  # Поддержка загрузки файлов


class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        current_day = timezone.now().strftime('%A')  # Получаем текущий день недели
        current_time = timezone.now().time()  # Получаем текущее время

        # Фильтрация расписания
        queryset = Schedule.objects.filter(
            Q(day_of_week=current_day) &
            Q(start_time__lte=current_time) &
            Q(end_time__gte=current_time)
        )
        return queryset
class CircleListCreateView(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer