from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('email', )
    search_fields = ['email']
