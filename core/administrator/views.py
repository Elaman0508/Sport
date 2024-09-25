from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Hall, Circle
from .serializers import *

class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
  # Support for file uploads

class HallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer # Support for file uploads

class CircleListCreateView(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class CircleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
class UserLoginView(generics.CreateAPIView):
    """User authentication."""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        # Token creation
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'response': True,
            'token': token.key
        }, status=status.HTTP_200_OK)

        # The following return would be unnecessary because of `is_valid(raise_exception=True)`
        # However, if you want to keep the validation, you can use the serializer's errors:
        # return Response({
        #     'response': False,
        #     'message': serializer.errors
        # }, status=status.HTTP_400_BAD_REQUEST)
class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# View for retrieving, updating, and deleting a specific Trainer
class TrainerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# View for listing and creating Clients
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# View for retrieving, updating, and deleting a specific Client
class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
