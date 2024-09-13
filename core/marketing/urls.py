from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import *

router = DefaultRouter()

router.register(r'advertisements', AdvertisementListCreateView)
router.register(r'tariffs', TariffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentListCreateView.as_view(), name='payments-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
