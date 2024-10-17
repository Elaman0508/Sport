import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import *
from rest_framework.exceptions import PermissionDenied
from .serializers import *
# hall
class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
    

class HallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]

#WorkSchedule
class WorkScheduleListCreateView(generics.ListCreateAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer

class WorkScheduleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
#Кружки
class CircleListCreateView(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]


class CircleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
#Schedul
class SchedulListCreateView(generics.ListCreateAPIView):
    queryset = Schedul.objects.all()
    serializer_class = SchedulSerializer

    def create(self, request, *args, **kwargs):
        schedules_data = request.data  # Получаем данные из запроса
        serializer = SchedulSerializer(data=schedules_data, many=True)  # Указываем many=True для массового создания
        serializer.is_valid(raise_exception=True)  # Проверяем данные на валидность
        serializer.save()  # Сохраняем все объекты
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SchedulRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedul.objects.all()
    serializer_class = SchedulSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
#login
class UserLoginView(generics.CreateAPIView):
    """User authentication for administrators only."""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        # Check if the user is an administrator
        if not user.is_staff and not user.is_superuser:
            raise PermissionDenied("Only administrators can log in.")

        # Token creation
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'response': True,
            'token': token.key
        }, status=status.HTTP_200_OK)
#Trainer
class TrainerCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    parser_classes = [MultiPartParser]
    parser_classes = [JSONParser]
# View for retrieving, updating, and deleting a specific Trainer
class TrainerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    parser_classes = [JSONParser]
#client
# View for listing and creating Clients
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    parser_classes = [MultiPartParser]

# View for retrieving, updating, and deleting a specific Client
class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Advertisement
class AdvertisementListCreateView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    parser_classes = [MultiPartParser]  # Обработка файлов
    #
    # def perform_create(self, serializer):
    #     serializer.save()  # Сохраняем объявление, включая поле photo

class AdvertisementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

#Schedule

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Представление для получения, обновления и удаления одного отзыва
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
#платеж
# Представление для списка и создания платежей
class PaymentListCreateView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
