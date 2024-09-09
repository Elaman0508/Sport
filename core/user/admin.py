from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Поля, которые будут отображаться в списке пользователей
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'birth_date',
        'activation_code',
        'activation_code_created_at',  # Добавляем это поле
        'reset_code',
        'is_active',
        'is_staff'
    )

    # Фильтры для панели
    list_filter = ('is_active', 'is_staff')

    # Разделы для редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
        'first_name', 'last_name', 'phone_number', 'birth_date', 'activation_code', 'activation_code_created_at',
        'reset_code')}),  # Добавляем сюда 'activation_code_created_at'
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Поля для добавления нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'birth_date'),
        }),
    )

    # По каким полям осуществляется поиск
    search_fields = ('email', 'first_name', 'last_name')

    # Сортировка
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
