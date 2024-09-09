from django.urls import path
from .views import TrainerListCreateView, ClientListView

urlpatterns = [
    path('trainers/', TrainerListCreateView.as_view(), name='trainer-list-create'),
    path('clients/', ClientListView.as_view(), name='client-list'),

]
