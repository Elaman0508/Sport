import stripe
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Advertisement, Tariff
from .serializers import AdvertisementSerializer, TariffSerializer
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(APIView):
    def post(self, request):
        try:
            token = request.data.get('token')
            amount = request.data.get('amount')

            # Создаем платеж в Stripe
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Сумма в центах
                currency="usd",
                description="Example charge",
                source=token,
            )
            return Response({'status': 'success', 'charge_id': charge.id})
        except stripe.error.StripeError as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

    def get(self, request):
        # Логика для обработки GET-запроса
        return Response({"message": "GET-запрос успешен"})

    def post(self, request):
        # Логика для обработки POST-запроса (например, создание платежа)
        return Response({"message": "POST-запрос успешен"})


class AdvertisementListCreateView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


# Retrieve, update, or delete a specific advertisement
# class AdvertisementDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
