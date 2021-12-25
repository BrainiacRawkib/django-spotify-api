from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Room
# Register your models here.

admin.site.register(Session)
admin.site.register(Room)
