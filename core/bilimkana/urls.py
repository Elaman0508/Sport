from django.urls import path
from .views import (
    ArenaListCreateAPIView, ArenaRetrieveUpdateDestroyAPIView,
    FeedbackListCreateView, FeedbackRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView,
    TrainerListCreateAPIView, TrainerRetrieveUpdateDestroyAPIView,
    ClassScheduleListCreateAPIView, ClassScheduleRetrieveUpdateDestroyAPIView,
    ClubInfoListCreateAPIView, ClubInfoRetrieveUpdateDestroyAPIView,
    RegistrationListCreateAPIView, RegistrationRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Arena
    path('bilimkana/arena/arenas/', ArenaListCreateAPIView.as_view(), name='bilimkana_arena_arenas_list'),
    path('bilimkana/arena/arenas/<int:pk>/', ArenaRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_arenas_read'),

    # Feedback
    path('bilimkana/arena/feedback/', FeedbackListCreateView.as_view(), name='bilimkana_arena_feedback_list'),  # Исправлено
    path('bilimkana/arena/feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_feedback_read'),

    # Reviews
    path('bilimkana/arena/reviews/', ReviewListCreateAPIView.as_view(), name='bilimkana_arena_reviews_list'),
    path('bilimkana/arena/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_reviews_read'),

    # Trainers
    path('bilimkana/arena/trainers/', TrainerListCreateAPIView.as_view(), name='bilimkana_arena_trainers_list'),
    path('bilimkana/arena/trainers/<int:pk>/', TrainerRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_trainers_read'),

    # Class Schedule
    path('bilimkana/arena/class-schedule/', ClassScheduleListCreateAPIView.as_view(), name='bilimkana_arena_class-schedule_list'),
    path('bilimkana/arena/class-schedule/<int:pk>/', ClassScheduleRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_class-schedule_read'),

    # Club Info
    path('bilimkana/arena/club-info/', ClubInfoListCreateAPIView.as_view(), name='bilimkana_arena_club-info_list'),
    path('bilimkana/arena/club-info/<int:pk>/', ClubInfoRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_club-info_read'),

    # Registrations
    path('bilimkana/arena/registrations/', RegistrationListCreateAPIView.as_view(), name='bilimkana_arena_registrations_list'),
    path('bilimkana/arena/registrations/<int:pk>/', RegistrationRetrieveUpdateDestroyAPIView.as_view(), name='bilimkana_arena_registrations_read'),
]