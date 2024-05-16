from django.contrib import admin
from .models import Teachers

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'created_at']
    class Meta:
        model = Teachers

