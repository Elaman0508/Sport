from django.db import models

class Hall(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    text = models.TextField(verbose_name='Текст')
    name = models.CharField(max_length=255, verbose_name='Название зала')
    dimensions = models.CharField(max_length=255, verbose_name='Размеры зала')
    capacity = models.PositiveIntegerField(verbose_name='Количество мест')
    type = models.CharField(max_length=100, verbose_name='Тип')
    covering = models.CharField(max_length=100, verbose_name='Покрытие')
    inventory = models.TextField(verbose_name='Инвентарь')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Оплата за час')
    title1 = models.CharField(max_length=255, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

class Review(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveIntegerField(verbose_name='Оценка')  # Оценка от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

class HallImage(models.Model):
    hall = models.ForeignKey(Hall, related_name='images', on_delete=models.CASCADE, verbose_name='Зал')
    image = models.ImageField(upload_to='hall_images/', verbose_name='Изображение')

    def __str__(self):
        return f'Изображение зала {self.hall}'

    class Meta:
        verbose_name = 'Изображение зала'
        verbose_name_plural = 'Изображения залов'
class Circle(models.Model):
    # Основные поля
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='circle_images/', verbose_name='Изображение', blank=True, null=True)

    # Дополнительные поля
    title1 = models.CharField(max_length=255, verbose_name='Дополнительное название')
    text = models.TextField(verbose_name='Текст')
    description1 = models.TextField(verbose_name='Дополнительное описание')
    video_link = models.URLField(max_length=500, verbose_name='Ссылка на видео', blank=True, null=True)

    text1 = models.TextField(verbose_name='Дополнительный текст', blank=True, null=True)
    description2 = models.TextField(verbose_name='Дополнительное описание', blank=True, null=True)

    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Кружки'
        verbose_name_plural = 'Кружки'


class CircleImage(models.Model):
    circle = models.ForeignKey(Circle, related_name='images', on_delete=models.CASCADE, verbose_name='Кружок')
    image = models.ImageField(upload_to='circle_images/', verbose_name='Изображение')

    def __str__(self):
        return f'Изображение кружка {self.circle.title}'

    class Meta:
        verbose_name = 'Изображение кружка'
        verbose_name_plural = 'Изображения кружков'


class TrainingSchedule(models.Model):
    TIME_CHOICES = [
        ('07:00', '07:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
    ]

    DAY_CHOICES = [
        ('Mon', 'Пн'),
        ('Tue', 'Вт'),
        ('Wed', 'Ср'),
        ('Thu', 'Чт'),
        ('Fri', 'Пт'),
        ('Sat', 'Сб'),
    ]

    time = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name='Время')
    day = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name='День')
    sport = models.CharField(max_length=255, verbose_name='Спорт')
    age_group = models.CharField(max_length=255, verbose_name='Возрастная группа')
    coach = models.CharField(max_length=255, verbose_name='Тренер')

    def __str__(self):
        return f'{self.day} {self.time} - {self.sport} ({self.age_group}) - {self.coach}'

    class Meta:
        verbose_name = 'Расписание тренировки'
        verbose_name_plural = 'Расписания тренировок'
