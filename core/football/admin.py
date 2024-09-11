from django.contrib import admin
from .models import Hall, Review, HallImage, CircleImage, Circle, TrainingSchedule


class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1  # Количество дополнительных пустых форм

class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'capacity', 'type', 'hourly_rate', 'address', 'phone')
    search_fields = ('title', 'name', 'description', 'text', 'title1')
    list_filter = ('type', 'capacity', 'covering')
    inlines = [HallImageInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_at')
    search_fields = ('user_name', 'text')
    list_filter = ('rating', 'created_at')

class HallImageAdmin(admin.ModelAdmin):
    list_display = ('hall', 'image')
    search_fields = ('hall__title',)  # Поиск по названию зала

admin.site.register(Hall, HallAdmin)
admin.site.register(Review, ReviewAdmin)
class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1  # Количество пустых форм для добавления изображений

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'phone')
    search_fields = ('title', 'description', 'address', 'phone')
    inlines = [CircleImageInline]

@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ('time', 'day', 'sport', 'age_group', 'coach')
    list_filter = ('day', 'time', 'sport', 'age_group')
    search_fields = ('sport', 'coach')
