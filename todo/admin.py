from django.contrib import admin
from .models import Task

# Register your models here.

# Admin-Konfiguration für das Task-Model
class TaskAdmin(admin.ModelAdmin):
    # Felder, die im Admin-Interface angezeigt werden sollen
    list_display = ('task', 'is_completed', 'created_at', 'updated_at')

    # Felder, die zur Suche im Admin-Interface genutzt werden können
    search_fields = ('task',)


# Models registrieren, damit sie im Admin-Interface angezeigt werden
admin.site.register(Task, TaskAdmin)