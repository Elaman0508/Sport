from datetime import timezone

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from .models import *
from .serializers import *

class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = (MultiPartParser, FormParser)  # Поддержка загрузки файлов
    permission_classes = [IsAuthenticated]  # Проверка авторизации

class HallRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = (MultiPartParser, FormParser)  # Поддержка загрузки файлов
    permission_classes = [IsAuthenticated]  # Проверка авторизации

class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]  # Проверка авторизации

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
    permission_classes = [IsAuthenticated]  # Проверка авторизации

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]  # Проверка авторизации

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    # Проверка авторизации
class AdminLoginView(generics.CreateAPIView):
    """Аутентификация пользователя администратора."""
    serializer_class = AdminLoginSerializer
    permission_classes = [IsAdminUser]  # Ограничиваем доступ только для администраторов

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'response': True,
            'token': token.key
        }, status=status.HTTP_200_OK)