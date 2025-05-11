from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('question', 'updated_on')
    search_fields = ['question', 'updated_on']
