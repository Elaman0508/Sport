from django.db import models
from django.contrib.auth import get_user_model


from django.conf import settings

User = get_user_model()


class SwimClass(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    is_free_for_new_users = models.BooleanField(default=True)
    img = models.ImageField(blank=True, null=True, upload_to='class_images/')

    def __str__(self):
        return self.name


class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Swim_registrations')
    basketball_class = models.ForeignKey(SwimClass, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.basketball_class.name}'


class Arena(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    flooring = models.CharField(max_length=255)
    court_count = models.IntegerField()
    equipment = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    changing_room = models.BooleanField(default=True)
    lighting = models.BooleanField(default=True)
    shower = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)  # Имя пользователя
    rating = models.IntegerField()  # Оценка (1-5)
    experience = models.TextField()  # Текст отзыва
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.name


class Review(models.Model):
    arena = models.ForeignKey(Arena, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Количество лет опыта")

    def __str__(self):
        return self.name


class ClassSchedule(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    ]
    class_name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time = models.TimeField()

    def __str__(self):
        return self.name


class ClubInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    advantages = models.TextField()
    client_reviews = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
