from django.contrib import admin
from .models import Room




class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)

admin.site.register(Room, RoomAdmin)
