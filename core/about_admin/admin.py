from django.contrib import admin
from django.utils import timezone
from .models import Hall, HallImage, Schedule, CircleImage, Circle
from django.db.models import Q

class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1  # Количество дополнительных форм для добавления изображений

class HallAdmin(admin.ModelAdmin):
    inlines = [HallImageInline]  # Включаем inline-форму для фотографий
    list_display = (
        'title', 'phone', 'address', 'size', 'quantity', 'hall_type',
        'coverage', 'hourly_rate', 'dressing_room', 'lighting', 'shower'
    )
    search_fields = ('title', 'phone', 'address', 'description')

admin.site.register(Hall, HallAdmin)

class HallImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'hall', 'image')
    search_fields = ('hall__title',)  # Поиск по названию зала

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['hall', 'start_time', 'end_time']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        current_time = timezone.now().time()  # Получаем текущее время

        # Фильтрация расписания
        queryset = queryset.filter(
            Q(start_time__lte=current_time) &
            Q(end_time__gte=current_time)
        )
        return queryset

admin.site.register(Schedule, ScheduleAdmin)

class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'address', 'sports']
    search_fields = ['title', 'phone', 'address']
    fieldsets = (
        (None, {'fields': ('title', 'sports', 'phone', 'address', 'images')}),
        ('Дополнительные данные', {'fields': (
            'header1', 'description1',
            'header2', 'description2',
            'header3', 'description3',
            'header4', 'description4'
        )}),
    )
    inlines = [CircleImageInline]

@admin.register(CircleImage)
class CircleImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
