from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'sent_on')
    search_fields = ['name', 'message', 'message']
    ordering = ('-sent_on',)
