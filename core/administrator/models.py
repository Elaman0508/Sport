from django.db import models

class Hall(models.Model):
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
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    description = models.TextField(verbose_name='Описание')
    sports = models.CharField(verbose_name='Виды спорта', max_length=20, choices=SPORT_CHOICES)
    size = models.CharField(verbose_name='Размеры зала', max_length=50)
    quantity = models.IntegerField(verbose_name='Количество')
    hall_type = models.CharField(verbose_name='Тип', max_length=100)
    coverage = models.CharField(verbose_name='Покрытие', max_length=100)
    inventory = models.TextField(verbose_name='Инвентарь')
    hourly_rate = models.DecimalField(verbose_name='Оплата за час', max_digits=10, decimal_places=2)
    dressing_room = models.BooleanField(verbose_name='Раздевалка', default=False)
    lighting = models.BooleanField(verbose_name='Освещение', default=False)
    shower = models.BooleanField(verbose_name='Душевая', default=False)
    day_of_week = models.CharField(verbose_name='День недели', max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(verbose_name='Начало работы')
    end_time = models.TimeField(verbose_name='Конец работы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class HallImage(models.Model):
    hall = models.ForeignKey(Hall, related_name='images', on_delete=models.CASCADE, verbose_name='Зал')
    image = models.ImageField(upload_to='hall_images/', verbose_name='Изображение')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание изображения')  # Дополнительное поле для описания

    def __str__(self):
        return f'Изображение зала {self.hall.title}'

    class Meta:
        verbose_name = 'Изображение зала'
        verbose_name_plural = 'Изображения залов'


class Circle(models.Model):
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
    AGE_GROUP_CHOICES = [
        ('adults', 'Взрослые'),
        ('teens', 'Подростки'),
        ('kids', 'Дети'),
    ]

    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    sports = models.CharField(verbose_name='Виды спорта', max_length=20, choices=SPORT_CHOICES)
    images = models.ManyToManyField('CircleImage', verbose_name='Фото', blank=True, related_name='circles')

    # Поля для заголовков и описаний
    header1 = models.CharField(verbose_name='Заголовок 1', max_length=255, blank=True)
    header2 = models.CharField(verbose_name='Заголовок 2', max_length=255, blank=True)
    header3 = models.CharField(verbose_name='Заголовок 3', max_length=255, blank=True)
    header4 = models.CharField(verbose_name='Заголовок 4', max_length=255, blank=True)
    description1 = models.TextField(verbose_name='Описание 1', blank=True)
    description2 = models.TextField(verbose_name='Описание 2', blank=True)
    description3 = models.TextField(verbose_name='Описание 3', blank=True)
    description4 = models.TextField(verbose_name='Описание 4', blank=True)
    age_group = models.CharField(verbose_name='Возрастная группа', max_length=10, choices=AGE_GROUP_CHOICES)
    day_of_week = models.CharField(verbose_name='День недели', max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(verbose_name='Начало занятий')
    end_time = models.TimeField(verbose_name='Конец занятий')
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

class Trainer(models.Model):
    SPORT_CHOICES = [
        ('basketball', 'Баскетбол'),
        ('football', 'Футбол'),
        ('volleyball', 'Волейбол'),
        ('tennis', 'Теннис'),
        ('boxing', 'Бокс'),
        ('cycling', 'Велоспорт'),
        ('taekwondo', 'Таэквондо'),
        ('swimming', 'Плавание'),
        ('yoga', 'Йога'),
    ]

    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    sport = models.CharField(verbose_name='Спорт', max_length=20, choices=SPORT_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

class Client(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('transfer', 'Перевод'),
    ]

    SPORT_CHOICES = [
        ('basketball', 'Баскетбол'),
        ('football', 'Футбол'),
        ('volleyball', 'Волейбол'),
        ('tennis', 'Теннис'),
        ('boxing', 'Бокс'),
        ('cycling', 'Велоспорт'),
        ('taekwondo', 'Таэквондо'),
        ('swimming', 'Плавание'),
        ('yoga', 'Йога'),
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
