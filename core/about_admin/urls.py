from django.urls import path
from .views import HallListCreateView, HallRetrieveUpdateDestroyView, ScheduleListView, CircleListCreateView

urlpatterns = [
    path('halls/', HallListCreateView.as_view(), name='hall-list-create'),
    path('halls/<int:pk>/', HallRetrieveUpdateDestroyView.as_view(), name='hall-retrieve-update-destroy'),
    path('schedules/', ScheduleListView.as_view(), name='schedule-list'),
    path('circles/', CircleListCreateView.as_view(), name='circle-list-create'),
]
