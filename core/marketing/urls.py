from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import AdvertisementListCreateView, TariffViewSet, payment_view

router = DefaultRouter()

router.register(r'advertisements', AdvertisementListCreateView)
router.register(r'tariffs', TariffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payment/', payment_view, name='payment_view'),
]
