import stripe
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Advertisement, Tariff
from .serializers import AdvertisementSerializer, TariffSerializer
from django.conf import settings
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .forms import *
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt  # Отключаем CSRF для простоты (не рекомендуется в реальных проектах)
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Обработка платежа
            cardholder_name = form.cleaned_data['cardholder_name']
            card_number = form.cleaned_data['card_number']
            expiry_date = form.cleaned_data['expiry_date']
            cvv = form.cleaned_data['cvv']
            amount = form.cleaned_data['amount']

            # Здесь вы можете добавить код для обработки платежа с использованием
            # платежного шлюза, например Stripe или PayPal.

            return JsonResponse({'status': 'success', 'message': 'Payment processed successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'})
    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed.'})


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


class AdvertisementCreateView(generics.CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
