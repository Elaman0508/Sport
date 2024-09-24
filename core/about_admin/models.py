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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    hall = models.ForeignKey(Hall, related_name='schedules', on_delete=models.CASCADE, verbose_name='Зал')
    day_of_week = models.CharField(verbose_name='День недели', max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(verbose_name='Начало работы')
    end_time = models.TimeField(verbose_name='Конец работы')

    def __str__(self):
        return f'{self.hall.title} - {self.day_of_week}'

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'


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


class Schedul(models.Model):  # Рекомендуется переименовать в Schedule
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

    circle = models.ForeignKey(Circle, related_name='schedules', on_delete=models.CASCADE, verbose_name='Кружок')
    age_group = models.CharField(verbose_name='Возрастная группа', max_length=10, choices=AGE_GROUP_CHOICES)
    day_of_week = models.CharField(verbose_name='День недели', max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(verbose_name='Начало занятий')
    end_time = models.TimeField(verbose_name='Конец занятий')

    def __str__(self):
        return f'{self.circle.title} ({self.age_group}) - {self.day_of_week}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
