from django.contrib import admin
from .models import UserProfile, Schedule, Attendance, Payment1


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

