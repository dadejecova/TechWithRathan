from django.contrib import admin
from .models import course, trainer, student

# Register your models here.

class courseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name', 'description','duration']
    list_filter = ['course_name']
    ordering = ['id']

class trainerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'expertise', 'joinin_date', 'trainer_photo']
    search_fields = ['last_name']
    ordering = ['id']

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'enrolled_course', 'trainer', 'is_active']
    search_fields = ['last_name']
    ordering = ['id']

admin.site.register(course, courseAdmin)
admin.site.register(trainer, trainerAdmin)
admin.site.register(student, studentAdmin)