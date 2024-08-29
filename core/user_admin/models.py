from django.db import models


class Trainer(models.Model):
    SPORT_CHOICES = [
        ('basketball', 'Баскетбол'),
        ('football', 'Футбол'),
        ('volleyball', 'Волейбол'),
        ('tennis', 'Тенис'),
        ('boxing', 'Бокс'),
        ('cycling', 'Велоспорт'),
        ('taekwondo', 'Таэквондо'),
        ('swimming', 'Плавание'),
        ('yoga', 'Йога'),
    ]

    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Телефон', max_length=20)
    sport = models.CharField('Спорт', max_length=20, choices=SPORT_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Client(models.Model):
    SPORT_CHOICES = [
        ('basketball', 'Баскетбол'),
        ('football', 'Футбол'),
        ('volleyball', 'Волейбол'),
        ('tennis', 'Тенис'),
        ('boxing', 'Бокс'),
        ('cycling', 'Велоспорт'),
        ('taekwondo', 'Таэквондо'),
        ('swimming', 'Плавание'),
        ('yoga', 'Йога'),
    ]

    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('transfer', 'Перевод'),
    ]

    name = models.CharField('Имя', max_length=100)
    trainer = models.ForeignKey(Trainer, related_name='clients', on_delete=models.CASCADE)
    sport = models.CharField('Спорт', max_length=20, choices=SPORT_CHOICES)
    payment = models.CharField('Оплата', max_length=20, choices=PAYMENT_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
