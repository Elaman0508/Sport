from django.urls import path
from .views import SportClassListCreateView, SportClassRetrieveUpdateDestroyView

urlpatterns = [
    path('sport-classes/', SportClassListCreateView.as_view(), name='sportclass-list-create'),
    path('sport-classes/<int:pk>/', SportClassRetrieveUpdateDestroyView.as_view(), name='sportclass-detail'),
    # другие маршруты
]