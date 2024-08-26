from django.db import models


class SportClass(models.Model):
    SPORT_CHOICES = [
        ('Basketball', 'Basketball'),
        ('Football', 'Football'),
        ('Tennis', 'Tennis'),
        ('Swimming', 'Swimming'),
        ('Volleyball', 'Volleyball'),
        ('Taekwondo', 'Taekwondo'),
        ('Boxing', 'Boxing'),
        ('Cycling', 'Cycling'),
        ('Yoga', 'Yoga'),
    ]

    sport_type = models.CharField(max_length=50, choices=SPORT_CHOICES)
    class_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.sport_type} - {self.class_name}"