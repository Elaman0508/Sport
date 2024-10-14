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

class Payment1Admin(admin.ModelAdmin):
    list_display = ('user', 'schedule', 'amount', 'paid', 'payment_date')  # Поля, отображаемые в списке
    list_filter = ('paid', 'payment_date')  # Фильтры для поиска
    search_fields = ('user__username', 'amount')  # Поля для поиска
    ordering = ('-payment_date',)  # Порядок сортировки по умолчанию

    # Настройка форм для редактирования
    fieldsets = (
        (None, {
            'fields': ('user', 'schedule', 'amount', 'paid')
        }),
        # Убираем payment_date из fieldsets
        # ('Дата платежа', {
        #     'fields': ('payment_date',),
        #     'classes': ('collapse',),  # Скрывает поле по умолчанию
        # }),
    )

    # Не нужно добавлять payment_date в read-only fields, так как оно не редактируется
    def get_readonly_fields(self, request, obj=None):
        return ['payment_date'] if obj else []

# Регистрация модели Payment1 с администратором
admin.site.register(Payment1, Payment1Admin)