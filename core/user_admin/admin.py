from django.contrib import admin
from .models import Trainer, Client

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sport')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('sport',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'sport', 'payment')
    search_fields = ('name', 'trainer__first_name', 'trainer__last_name')
    list_filter = ('sport', 'payment', 'trainer')
