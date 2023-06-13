from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'voted_president', 'voted_vice_president',
                    'voted_secretary', 'voted_treasurer', 'voted_wocom']
