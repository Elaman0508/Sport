import stripe
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from django.conf import settings
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentListCreateView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


def post(self, request, *args, **kwargs):
    # Получение данных из формы
    card_holder_name = request.data.get('card_holder_name')
    card_number = request.data.get('card_number')
    expiry_date = request.data.get('expiry_date')
    cvc = request.data.get('cvc')

    # Вывод данных для отладки
    print("Received data:", {
        "card_holder_name": card_holder_name,
        "card_number": card_number,
        "expiry_date": expiry_date,
        "cvc": cvc,
    })

    # Проверка наличия всех необходимых данных
    if not all([card_holder_name, card_number, expiry_date, cvc, ]):
        return Response({"error": "Пожалуйста, заполните все поля формы."}, status=status.HTTP_400_BAD_REQUEST)

    # Проверка формата expiry_date
    if '/' not in expiry_date:
        return Response({"error": "Неверный формат даты истечения срока. Используйте MM/YY."},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        # Разделение даты истечения срока на месяц и год
        exp_month, exp_year = expiry_date.split('/')
        exp_month = int(exp_month)
        exp_year = int(exp_year)

        # Создание токена карты через Stripe
        token = stripe.Token.create(
            card={
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )

        # Создание платежа через Stripe
        charge = stripe.Charge.create(
            source=token.id,
        )

        # Сохранение информации о платеже в базе данных
        payment = Payment.objects.create(
            card_holder_name=card_holder_name,
            card_number=card_number,
            expiry_date=expiry_date,
            cvc=cvc
        )
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except stripe.error.StripeError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({"error": "Ошибка при разборе даты истечения срока: " + str(e)},
                        status=status.HTTP_400_BAD_REQUEST)


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
