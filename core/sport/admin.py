from django.contrib import admin
from .models import (
    Sport,
    Hall,
    HallInfo,
    HallArena,
    Club,
    ClubAdditionalInfo,
    ClubImage,
    Review,
    HallImage,
    TrainingSchedule,
)

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'sport')
    search_fields = ('title',)
    list_filter = ('sport',)

@admin.register(HallInfo)
class HallInfoAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    inlines = [HallImageInline]

@admin.register(HallArena)
class HallArenaAdmin(admin.ModelAdmin):
    list_display = ('title', 'capacity')  # Убедитесь, что все поля существуют
    search_fields = ('title', 'hall__title')
    list_filter = ('hall',) if hasattr(HallArena, 'hall') else []  # Аналогичная проверка для 'hall'

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    list_display = ('title', 'sport')
    search_fields = ('title',)
    list_filter = ('sport',)
    inlines = [ClubImageInline]

admin.site.register(Club, ClubAdmin)


@admin.register(ClubAdditionalInfo)
class ClubAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone')
    search_fields = ('title', 'description', 'address')
    list_filter = ('address',)  # Убедитесь, что используете правильные поля
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('club', 'title', 'subtitle', 'description', 'video_link', 'address', 'phone')
        }),
        ('Дополнительная информация', {
            'fields': ('details',)  # Используйте более описательные названия
        }),
    )
    inlines = [ClubImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_at', 'sport')
    search_fields = ('user_name', 'text')
    list_filter = ('sport', 'rating',)

@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'time', 'sport', 'age_group', 'coach')
    search_fields = ('sport__name', 'coach')
    list_filter = ('day', 'sport',)
