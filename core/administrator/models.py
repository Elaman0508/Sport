from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
class Hall(models.Model):
    SPORT_CHOICES = [
        ('Баскетбол', 'Баскетбол'),
        ('Футбол', 'Футбол'),
        ('Валейбол', 'Валейбол'),
        ('Тенис', 'Тенис'),
        ('Бокс', 'Бокс'),
        ('Велоспорт', 'Велоспорт'),
        ('Таэквондо', 'Таэквондо'),
        ('Плавание', 'Плавание'),
        ('Йога', 'Йога'),
    ]
    sports = models.CharField(verbose_name='Виды спорта', max_length=20, choices=SPORT_CHOICES)
    image = models.ImageField(upload_to='hall_images/', verbose_name='Изображение')
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    size = models.CharField(verbose_name='Размеры', max_length=50)  # Размеры зала
    inventory = models.TextField(verbose_name='Инвентарь')  # Описание инвентаря
    price_per_hour = models.DecimalField(verbose_name='Оплата за час', max_digits=10, decimal_places=2)  # Цена за час
    quantity = models.IntegerField(verbose_name='Количество')  # Количество мест
    coverage = models.CharField(verbose_name='Покрытие', max_length=100)  # Покрытие
    hall_type = models.CharField(verbose_name='Тип', max_length=100)  # Тип зала
    shower = models.BooleanField(default=False, verbose_name='Душевая')  # Душевая
    lighting = models.BooleanField(default=False, verbose_name='Освещение')  # Освещение
    dressing_room = models.BooleanField(default=False, verbose_name='Раздевалка')  # Раздевалка
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
#
class HallImage(models.Model):
    hall = models.ForeignKey(Hall, related_name='images', on_delete=models.CASCADE, verbose_name='Зал')
    image = models.ImageField(upload_to='hall_images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение зала'
        verbose_name_plural = 'Изображения залов'

class WorkSchedule(models.Model):
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
    # Поле по умолчанию True
    is_active = models.BooleanField(default=True, verbose_name="Активное расписание (True)")
    class Meta:
        unique_together = ('day_of_week', 'opening_time')
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
    def __str__(self):
        return f"{self.day_of_week}: {self.opening_time} - {self.closing_time}"


#Кружки
class Circle(models.Model):
    SPORT_CHOICES = [
        ('Баскетбол', 'Баскетбол'),
        ('Футбол', 'Футбол'),
        ('Валейбол', 'Валейбол'),
        ('Тенис', 'Тенис'),
        ('Бокс', 'Бокс'),
        ('Велоспорт', 'Велоспорт'),
        ('Таэквондо', 'Таэквондо'),
        ('Плавание', 'Плавание'),
        ('Йога', 'Йога'),
    ]
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    image = models.ImageField(upload_to='circle_images/', verbose_name='Фото')
    sports = models.CharField(verbose_name='Виды спорта', max_length=20, choices=SPORT_CHOICES)
    header1 = models.CharField(verbose_name='Заголовок 1', max_length=255, blank=True)
    description1 = models.TextField(verbose_name='Описание 1', blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    header2 = models.CharField(verbose_name='Заголовок 2', max_length=255, blank=True)
    description2 = models.TextField(verbose_name='Описание 2', blank=True)
    header3 = models.CharField(verbose_name='Заголовок 3', max_length=255, blank=True)
    description3 = models.TextField(verbose_name='Описание 3', blank=True)
    header4 = models.CharField(verbose_name='Заголовок 4', max_length=255, blank=True)
    description4 = models.TextField(verbose_name='Описание 4', blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'


class CircleImage(models.Model):
    image = models.ImageField(upload_to='circle_images/', verbose_name='Фото')
    circle = models.ForeignKey(Circle, related_name='circle_images', on_delete=models.CASCADE, verbose_name='Кружок')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание изображения')  # Дополнительное поле для описания
    def __str__(self):
        return f'Изображение {self.id}'
    class Meta:
        verbose_name = 'Фото кружка'
        verbose_name_plural = 'Фото кружков'

class Schedul(models.Model):
    CATEGORY_CHOICES = (
        ('adults', 'Взрослые'),
        ('teens', 'Подростки'),
        ('kids', 'Дети'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Категория")
    day_of_week = models.CharField(max_length=15, verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Начало занятия")
    end_time = models.TimeField(verbose_name="Окончание занятия", null=True, blank=True)
    category1 = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Категория")
    day_of_week1 = models.CharField(max_length=15, verbose_name="День недели")
    start_time1 = models.TimeField(verbose_name="Начало занятия")
    end_time1 = models.TimeField(verbose_name="Окончание занятия", null=True, blank=True)
    category2 = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Категория")
    day_of_week2 = models.CharField(max_length=15, verbose_name="День недели")
    start_time2 = models.TimeField(verbose_name="Начало занятия")
    end_time2 = models.TimeField(verbose_name="Окончание занятия", null=True, blank=True)
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
    def __str__(self):
        return f'{self.get_category_display()} - {self.day_of_week}'

#Тренеры
class Trainer(models.Model):
    SPORT_CHOICES = [
        ('Баскетбол', 'Баскетбол'),
        ('Футбол', 'Футбол'),
        ('Валейбол', 'Валейбол'),
        ('Тенис', 'Тенис'),
        ('Бокс', 'Бокс'),
        ('Велоспорт', 'Велоспорт'),
        ('Таэквондо', 'Таэквондо'),
        ('Плавание', 'Плавание'),
        ('Йога', 'Йога'),
    ]
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    photo = models.ImageField(verbose_name='Фото', upload_to='trainers_photos/', blank=True, null=True)
    sport = models.CharField(verbose_name='Спорт', max_length=20, choices=SPORT_CHOICES)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
#Клиенты
class Client(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Наличные', 'Наличные'),
        ('Карта', 'Карта'),
        ( 'Перевод', 'Перевод'),
    ]
    SPORT_CHOICES = [
        ('Баскетбол', 'Баскетбол'),
        ('Футбол', 'Футбол'),
        ('Валейбол', 'Валейбол'),
        ('Тенис', 'Тенис'),
        ('Бокс', 'Бокс'),
        ('Велоспорт', 'Велоспорт'),
        ('Таэквондо', 'Таэквондо'),
        ('Плавание', 'Плавание'),
        ('Йога', 'Йога'),
    ]
    name = models.CharField(verbose_name='Имя', max_length=255)
    trainer = models.ForeignKey(Trainer, related_name='clients', on_delete=models.CASCADE, verbose_name='Тренер')
    sport = models.CharField(verbose_name='Спорт', max_length=20, choices=SPORT_CHOICES)
    payment_method = models.CharField(verbose_name='Метод оплаты', max_length=10, choices=PAYMENT_METHOD_CHOICES)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
#реклама
class Advertisement(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    site_link = models.URLField()
    installment_plan = models.CharField(max_length=255)
  # Основное изображение объявления

    class Meta:
        verbose_name = "реклама"
        verbose_name_plural = "реклама"

    def __str__(self):
        return self.title
#отзыв
class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.PositiveIntegerField(verbose_name="Рейтинг", default=0)
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']  # Сортировка по дате создания (последние отзывы первыми)
    def __str__(self):
        return f"{self.name}: {self.comment[:20]}"

class Payment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    sport = models.CharField(max_length=50, verbose_name="Спорт")
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за месяц")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Убедитесь, что это поле есть
    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
    def __str__(self):
        return f"{self.name} - {self.sport} - {self.monthly_price} руб."
