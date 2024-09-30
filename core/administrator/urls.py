from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# Создаем роутер
router = DefaultRouter()

# Основные URL маршруты
urlpatterns = [
    path('halls/', HallListCreateView.as_view(), name='hall-list-create'),
    path('halls/<int:pk>/', HallRetrieveUpdateDestroyView.as_view(), name='hall-retrieve-update-destroy'),
    path('schedul/', SchedulListCreateView.as_view(), name='schedul-list'),
    path('schedul/<int:pk>/', SchedulRetrieveUpdateDestroyView.as_view(), name='schedul-detail'),
    path('/circles/', CircleListCreateView.as_view(), name='circle-list-create'),  # Путь для администратора
    path('/circles/<int:pk>/', CircleRetrieveUpdateDestroyView.as_view(), name='circle-retrieve-update-destroy'),  # Путь для администратора с pk
    path('login/', UserLoginView.as_view(), name='login'),
    path('trainers/', TrainerCreateView.as_view(), name='trainer-list-create'),
    path('trainers/<int:pk>/', TrainerRetrieveUpdateDestroyView.as_view(), name='trainer-detail'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    # URL для списка и создания объявлений
    path('advertisements/', AdvertisementListCreateView.as_view(), name='advertisement-list-create'),
    # URL для получения, обновления и удаления одного объявления
    path('advertisements/<int:pk>/', AdvertisementRetrieveUpdateDestroyView.as_view(), name='advertisement-detail'),
    # URL для списка и создания расписаний
    path('schedules/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    # URL для получения, обновления и удаления одного расписания
    path('schedules/<int:pk>/', ScheduleRetrieveUpdateDestroyView.as_view(), name='schedule-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),

    # URL для получения, обновления и удаления одного отзыва
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),

]

# Добавляем маршруты роутера к urlpatterns
urlpatterns += router.urls