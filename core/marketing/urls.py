from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import AdvertisementListCreateView, TariffViewSet, PaymentView

router = DefaultRouter()

router.register(r'advertisements', AdvertisementListCreateView)
router.register(r'tariffs', TariffViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentView.as_view(), name='payments'),
]
