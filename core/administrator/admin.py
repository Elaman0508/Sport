from django.contrib import admin
from .models import *
class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1
    verbose_name = 'Изображение зала'
    verbose_name_plural = 'Изображения залов'

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'sports', 'size', 'quantity', 'hourly_rate', 'dressing_room', 'lighting', 'shower', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('title', 'address', 'sports')
    list_filter = ('sports', 'day_of_week', 'dressing_room', 'lighting', 'shower')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'phone', 'address', 'description', 'sports', 'size', 'quantity', 'hall_type', 'coverage', 'inventory', 'hourly_rate', 'dressing_room', 'lighting', 'shower', 'day_of_week', 'start_time', 'end_time')
        }),
    )
class CircleImageInline(admin.TabularInline):
    model = CircleImage
    extra = 1
    verbose_name = 'Изображение кружка'
    verbose_name_plural = 'Изображения кружков'

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'address', 'sports', 'age_group', 'day_of_week', 'start_time', 'end_time']
    search_fields = ['title', 'phone', 'address', 'sports']
    list_filter = ['sports', 'age_group', 'day_of_week']

    # Inline для отображения изображений на странице кружков
    inlines = [CircleImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'phone', 'address', 'sports', 'age_group', 'day_of_week', 'start_time', 'end_time')
        }),
        ('Заголовки и описания', {
            'fields': ('header1', 'description1', 'header2', 'description2', 'header3', 'description3', 'header4', 'description4'),
        }),
    )

@admin.register(CircleImage)
class CircleImageAdmin(admin.ModelAdmin):
    list_display = ('circle', 'image')
    search_fields = ('circle__title',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sport')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('sport',)
    ordering = ('last_name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'sport', 'payment_method')  # Use existing field 'name'
    search_fields = ('name', 'trainer__first_name', 'trainer__last_name')  # Update for the existing field
    list_filter = ('sport', 'trainer')
    ordering = ('name',)  # Use 'name' for ordering
