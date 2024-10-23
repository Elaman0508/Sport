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


@admin.register(Payment1)
class Payment1Admin(admin.ModelAdmin):
    list_display = ('user',  'sport', 'enrollment_date', 'paid')
    list_filter = ( 'sport', 'paid', 'day_of_week', 'is_active')
    search_fields = ('user__username', 'sport')
    ordering = ['-enrollment_date']
    fieldsets = (
        (None, {
            'fields': ('user',  'sport', 'schedule', 'day_of_week', 'opening_time', 'closing_time', 'paid')
        }),
        ('Дополнительная информация', {
            'fields': ('enrollment_date', 'is_active'),
            'classes': ('collapse',),
        }),
    )

# Регистрация модели Payment1 с администратором