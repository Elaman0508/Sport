from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register the viewsets
router = DefaultRouter()

urlpatterns = [
    path('halls/', HallListCreateView.as_view(), name='hall-list-create'),
    path('halls/<int:pk>/', HallRetrieveUpdateDestroyView.as_view(), name='hall-retrieve-update-destroy'),
    path('circles/', CircleListCreateView.as_view(), name='circle-list-create'),
    path('circles/<int:pk>/', CircleRetrieveUpdateDestroyView.as_view(), name='circle-retrieve-update-destroy'),
    path('login/', UserLoginView.as_view(), name='login'),
]

# Include the router's URLs in your urlpatterns if you have any viewsets registered
urlpatterns += router.urls
