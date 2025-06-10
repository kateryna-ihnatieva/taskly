from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "is_completed"]
    search_fields = ["title", "description"]
    list_editable = ["is_completed"]
