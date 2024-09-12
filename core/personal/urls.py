from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet, AttendanceViewSet, Payment1ViewSet

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'payments', Payment1ViewSet)

urlpatterns = [
    path('personal/', include(router.urls)),
]