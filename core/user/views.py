from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .serializers import UserRegistrationSerializer
from .models import CustomUser
from .utils import send_sms

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()

                # Получаем телефонный номер
                phone_number = serializer.validated_data.get("phone_number")
                phone_number = "".join(filter(str.isdigit, phone_number))  # Удаляем все нецифровые символы

                # Проверяем, что номер содержит 10 цифр
                if len(phone_number) != 10:
                    return Response(
                        {
                            "response": False,
                            "message": "Номер телефона должен содержать 10 цифр."
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                user = get_object_or_404(CustomUser, phone_number=phone_number)

                # Извлекаем код подтверждения
                sms_code = getattr(user, 'code', None)

                # Отправляем SMS с кодом подтверждения
                sms = send_sms(phone_number, "На адрес CMC, который вы указали, должен был прийти четырехзначный код.", sms_code)
                if sms:
                    return Response(
                        {
                            "response": True,
                            "message": "Код подтверждения был отправлен на ваш номер."
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {
                            "response": False,
                            "message": "Что-то пошло не так с отправкой SMS!"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except IntegrityError:
                return Response(
                    {"email": "Пользователь с таким адресом электронной почты уже существует."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
