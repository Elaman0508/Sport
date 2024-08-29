from django.urls import path
from .views import *

urlpatterns = [
    path('halls/', HallListView.as_view(), name='hall-list'),
    path('halls/<int:pk>/', HallDetailView.as_view(), name='hall-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('circles/', CircleListView.as_view(), name='circle-list'),
    path('circles/<int:pk>/', CircleDetailView.as_view(), name='circle-detail'),
    path('training-schedules/', TrainingScheduleListView.as_view(), name='training-schedule-list'),

]
