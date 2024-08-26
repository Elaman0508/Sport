from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'advertisements', AdvertisementListCreateView)
router.register(r'tariffs', TariffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentListCreateView.as_view(), name='payments-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
]
