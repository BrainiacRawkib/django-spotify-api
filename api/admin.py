from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ['code', 'host']


admin.site.register(Session)
