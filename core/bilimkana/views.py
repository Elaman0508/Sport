from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Arena, Feedback, Review, Trainer, ClassSchedule, ClubInfo, Registration
from .serializers import ArenaSerializer, FeedbackSerializer, ReviewSerializer, TrainerSerializer, \
    ClassScheduleSerializer, ClubInfoSerializer, RegistrationSerializer


# Arena Views
class ArenaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Arena.objects.all()
    serializer_class = ArenaSerializer


class ArenaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arena.objects.all()
    serializer_class = ArenaSerializer


# Feedback Views
class FeedbackListCreateView(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


# Review Views
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Trainer Views
class TrainerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


# Class Schedule Views
class ClassScheduleListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer


class ClassScheduleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer


# Club Info Views
class ClubInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClubInfo.objects.all()
    serializer_class = ClubInfoSerializer


class ClubInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClubInfo.objects.all()
    serializer_class = ClubInfoSerializer


# Registration Views
class RegistrationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
