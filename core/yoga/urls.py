from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'arenas', ArenaViewSet)
router.register(r'feedback', FeedbackViewSet, basename='feedback')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'trainers', TrainerViewSet)
router.register(r'class-schedule', ClassScheduleViewSet)
router.register(r'club-info', ClubInfoViewSet)
router.register(r'registrations', RegistrationViewSet, basename='registrations')


urlpatterns = [
    path('yoga/', include(router.urls)),
]
