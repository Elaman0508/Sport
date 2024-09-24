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
    inlines = [HallImageInline]

@admin.register(HallInfo)
class HallInfoAdmin(admin.ModelAdmin):
    list_display = ('hall', 'description')
    search_fields = ('description',)
    list_filter = ('hall',)
    inlines = [HallImageInline]

@admin.register(HallArena)
class HallArenaAdmin(admin.ModelAdmin):
    list_display = ('hall', 'title', 'capacity')
    search_fields = ('title', 'hall__title')
    list_filter = ('hall',)

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    list_display = ('title', 'sport')
    search_fields = ('title',)
    inlines = [ClubImageInline]

admin.site.register(Club, ClubAdmin)
@admin.register(ClubAdditionalInfo)
class ClubAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('club', 'title')
    search_fields = ('title',)
    inlines = [ClubImageInline]  # Add the inline for ClubImage

class ClubImageAdmin(admin.ModelAdmin):
    list_display = ('club',)
    search_fields = ('club__title',)

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
