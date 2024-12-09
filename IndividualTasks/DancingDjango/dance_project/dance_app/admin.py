from django.contrib import admin
from .models import Dancer, Group, Festival

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')

@admin.register(Dancer)
class DancerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'style', 'group')
    list_filter = ('style', 'group')
    search_fields = ('name',)

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'group')
    list_filter = ('date', 'group')
    search_fields = ('name',)

