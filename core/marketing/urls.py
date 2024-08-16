from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import AdvertisementListCreateView
router = DefaultRouter()

router.register(r'advertisements', AdvertisementListCreateView)


urlpatterns = [
    path('', include(router.urls)),
]