from django.db import models
from django.conf import settings  # Импортируем settings для использования кастомной модели пользователя
from django.contrib.auth.models import User

SPORT_CHOICES = [
    ('basketball', 'Баскетбол'),
    ('football', 'Футбол'),

    ('tennis', 'Теннис'),
    ('swimming', 'Плавание'),
    ('volleyball', 'Волейбол'),
    ('taekwondo', 'Тхэквондо'),
    ('boxing', 'Бокс'),
    ('cycling', 'Велоспорт'),
    ('yoga', 'Йога'),
]

# Модель Спорта
class Sport(models.Model):
    name = models.CharField(max_length=50, choices=SPORT_CHOICES, verbose_name="Вид спорта")

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'


class Schedule(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sport.name} - {self.date}"


class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)  # Ссылка на кастомную модель пользователя
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.schedule}"


class Payment1(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"  # Читаемое имя для поля user
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name="Расписание"  # Читаемое имя для поля schedule
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма"  # Читаемое имя для поля amount
    )
    paid = models.BooleanField(
        default=False,
        verbose_name="Оплачено"  # Читаемое имя для поля paid
    )
    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата платежа"  # Читаемое имя для поля payment_date
    )

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.paid}"

    class Meta:
        ordering = ['-payment_date']
        verbose_name = "Платеж"  # Имя в единственном числе
        verbose_name_plural = "Платежи"  # Имя во множественном числе


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name