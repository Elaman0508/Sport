from django.contrib import admin
from .models import Hall, HallImage, Review, Circle, CircleImage, TrainingSchedule

class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1

class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'capacity', 'type', 'address', 'phone')
    search_fields = ('title', 'name', 'address')
    list_filter = ('type', 'dressing_room', 'lighting', 'shower')
    inlines = [HallImageInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating', 'created_at')
    search_fields = ('user_name', 'text')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1

class CircleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'phone')
    search_fields = ('title', 'description', 'address')
    inlines = [CircleImageInline]

class TrainingScheduleAdmin(admin.ModelAdmin):
    list_display = ('time', 'day', 'sport', 'age_group', 'coach')
    list_filter = ('day', 'sport', 'age_group')
    ordering = ('day', 'time')

admin.site.register(Hall, HallAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Circle, CircleAdmin)
admin.site.register(TrainingSchedule, TrainingScheduleAdmin)
