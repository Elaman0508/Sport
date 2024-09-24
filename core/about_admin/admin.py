from django.contrib import admin
from .models import Hall, Schedule, HallImage, Circle, CircleImage, Schedul  # Переименуйте Schedul в Schedule, если нужно

class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1
    verbose_name = 'Изображение зала'
    verbose_name_plural = 'Изображения залов'
class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1
    verbose_name = 'График работы'
    verbose_name_plural = 'Графики работы'

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'sports', 'hourly_rate')
    search_fields = ('title', 'address')
    inlines = [HallImageInline]
    list_filter = ('sports',)
    inlines = [ScheduleInline]

    ordering = ('title',)


class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1
    verbose_name = 'Изображение кружка'
    verbose_name_plural = 'Изображения кружков'
class SchedulInline(admin.TabularInline):
    model = Schedul
    extra = 1
    verbose_name = 'График работы'
    verbose_name_plural = 'Графики работы'
@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'sports')
    search_fields = ('title', 'address')
    inlines = [HallImageInline]
    inlines = [SchedulInline]

@admin.register(CircleImage)
class CircleImageAdmin(admin.ModelAdmin):
    list_display = ('circle', 'image')
    search_fields = ('circle__title',)

@admin.register(Schedul)  # Переименуйте в Schedule
class SchedulAdmin(admin.ModelAdmin):  # Переименуйте в ScheduleAdmin, если нужно
    list_display = ('circle', 'age_group', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('circle__title',)
    list_filter = ('age_group', 'day_of_week')

admin.site.register(Schedule)  # Зарегистрируйте модель Schedule, если она переименована
