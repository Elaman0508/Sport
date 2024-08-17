from django.db import models


class Advertisement(models.Model):
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    description = models.TextField()
    training_zones = models.CharField(max_length=255)
    pool = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    schedule_day = models.CharField(max_length=50)
    working_hours = models.CharField(max_length=50)
    installment_period = models.CharField(max_length=10,
                                          choices=[('6', '6 months'), ('9', '9 months'), ('12', '12 months')])
    website_name = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.URLField(max_length=255, blank=True, null=True)
    tariffs = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Tariff(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()  # Количество дней действия тарифа

    def __str__(self):
        return self.name


class Payment(models.Model):
    card_holder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_holder_name


class Savephoto(models.Model):
    file = models.FileField(upload_to='uploads/')
