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
    AGE_CHOICES = [
        ('Взрослые', 'Взрослые'),
        ('Подростки', 'Подростки'),
        ('Дети', 'Дети')
    ]

    SPORTS_CHOICES = [
        ('Баскетбол', 'Баскетбол'),
        ('Футбол', 'Футбол'),
        ('Волейбол', 'Волейбол'),
        ('Тенис', 'Тенис'),
        ('Бокс', 'Бокс'),
        ('Велоспорт', 'Велоспорт'),
        ('Таэквондо', 'Таэквондо'),
        ('Плавание', 'Плавание'),
        ('Йога', 'Йога'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
        verbose_name="Возрастная группа"
    )
    sport = models.CharField(
        max_length=20,
        choices=SPORTS_CHOICES,
        verbose_name="Спорт"
    )
    paid = models.BooleanField(
        default=False,
        verbose_name="Оплачено"
    )
    enrollment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата записи"
    )
    day_of_week = models.CharField(
        max_length=12,
        choices=[
            ('Понедельник', 'Понедельник'),
            ('Вторник', 'Вторник'),
            ('Среда', 'Среда'),
            ('Четверг', 'Четверг'),
            ('Пятница', 'Пятница'),
            ('Суббота', 'Суббота'),
            ('Воскресенье', 'Воскресенье'),
        ],
        verbose_name="День недели"
    )
    opening_time = models.TimeField(verbose_name="Время открытия")
    closing_time = models.TimeField(verbose_name="Время закрытия")
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активное расписание (True)"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name