from django.contrib import admin
from .models import *
class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1  # Позволяет добавлять изображения напрямую в админке для каждого зала

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone', 'price_per_hour', 'quantity', 'hall_type')  # Отображаемые поля в списке
    list_filter = ('sports', 'hall_type', 'shower', 'lighting', 'dressing_room')  # Фильтры по полям
    search_fields = ('title', 'address', 'description')  # Поиск по заголовку, адресу и описанию
    inlines = [HallImageInline]  # Включаем изображения в страницу зала # Удобный интерфейс для выбора нескольких видов спорта

@admin.register(HallImage)
class HallImageAdmin(admin.ModelAdmin):
    list_display = ('hall', 'image')  # Отображаемые поля
    search_fields = ('hall__title',)  # Поиск по названию зала


class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'opening_time', 'closing_time','is_active')
    list_filter = ('day_of_week',)
    search_fields = ('day_of_week',)

admin.site.register(WorkSchedule, WorkScheduleAdmin)
class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1  # Количество пустых полей для добавления новых изображений

# Настройка отображения модели Circle
@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sports', 'phone', 'address')  # Поля, отображаемые в списке кружков
    search_fields = ('title', 'sports')  # Поля, по которым можно искать кружки
    inlines = [CircleImageInline]  # Отображение связанных изображений на странице кружка
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'sports', 'phone', 'address'),
        }),
        ('Описание секций', {
            'fields': ('header1', 'description1', 'header2', 'description2', 'header3', 'description3', 'header4', 'description4'),
            'classes': ('collapse',),  # Свернутый блок
        }),
    )

class CircleImageAdmin(admin.ModelAdmin):
    list_display = ('circle', 'image', 'description')  # Поля, отображаемые в списке изображений
    search_fields = ('circle__title', 'description')

class SchedulAdmin(admin.ModelAdmin):
    list_display = ('category', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('day_of_week',)
    list_filter = ('category',)
    ordering = ('day_of_week', 'start_time')

    def get_queryset(self, request):
        # Переопределяем метод для отображения всех записей
        return super().get_queryset(request)

    def save_model(self, request, obj, form, change):
        # Сохраняем объект и вызываем родительский метод
        super().save_model(request, obj, form, change)

admin.site.register(Schedul, SchedulAdmin)
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sport','photo')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('sport',)
    ordering = ('last_name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'sport', 'payment_method')  # Use existing field 'name'
    search_fields = ('name', 'trainer__first_name', 'trainer__last_name')  # Update for the existing field
    list_filter = ('sport', 'trainer')
    ordering = ('name',)  # Use 'name' for ordering


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'site_name')  # Отображаемые поля в админке
    search_fields = ('title', 'phone', 'address', 'site_name')  # Поля для поиска

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'rating')
    search_fields = ('name', 'comment')
    list_filter = ('rating', 'created_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'monthly_price', 'created_at')
    search_fields = ('name', 'sport')
    ordering = ('-created_at',)

    def created_at(self, obj):
        return obj.created_at

    created_at.short_description = 'Дата создания'  # Настраиваем имя столбца
