from django.contrib import admin
from .models import Hall, HallImage, Schedule, Circle, CircleImage, Trainer, Client

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'sports', 'size', 'quantity', 'hourly_rate')
    search_fields = ('title', 'address', 'sports')
    list_filter = ('sports', 'hall_type')

@admin.register(HallImage)
class HallImageAdmin(admin.ModelAdmin):
    list_display = ('hall', 'image')
    search_fields = ('hall__title',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('hall', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('hall__title',)
    list_filter = ('day_of_week', 'hall')

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'sports')
    search_fields = ('title', 'address', 'sports')
    list_filter = ('sports',)

@admin.register(CircleImage)
class CircleImageAdmin(admin.ModelAdmin):
    list_display = ('circle', 'image')
    search_fields = ('circle__title',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sport')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('sport',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'sport', 'payment')
    search_fields = ('name', 'trainer__first_name', 'trainer__last_name')
    list_filter = ('payment',)

# Регистрация моделей в админке
