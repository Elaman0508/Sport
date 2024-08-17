from django.contrib import admin
from .models import Advertisement, Tariff, Payment


admin.site.register(Advertisement)
admin.site.register(Tariff)
admin.site.register(Payment)