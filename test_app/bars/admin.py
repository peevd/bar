from django.contrib import admin
from .models import Bar

@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rating", "created_at", "updated_at")
    search_fields = ("name", "rating")
