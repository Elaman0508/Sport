from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'birth_date', 'gender', 'address')

    def full_name(self, obj):
        return obj.user.get_full_name()

    full_name.short_description = 'ФИО'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('sport', 'date', 'price')

    def sport(self, obj):
        return obj.sport.name

    sport.short_description = 'Спорт'


class Payment1Admin(admin.ModelAdmin):
    list_display = ('user', 'sport', 'paid', 'enrollment_date', 'is_active')
    list_filter = ('sport', 'paid', 'is_active')
    search_fields = ('user__username', 'sport')
    ordering = ('-enrollment_date',)

class SchedulAdmin(admin.ModelAdmin):
    list_display = ('circle', 'day_of_week', 'category', 'start_time', 'end_time', 'is_active')
    list_filter = ('day_of_week', 'category', 'is_active')
    search_fields = ('circle__user__username', 'category')
    ordering = ('day_of_week', 'start_time')

# Регистрация моделей в админ-панели
admin.site.register(Payment1, Payment1Admin)
admin.site.register(Schedul, SchedulAdmin)

# Регистрация модели Payment1 с администратором