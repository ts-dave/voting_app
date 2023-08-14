from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_active', 'voted']
    # TODO: Make voted FIELD READONLY BEFORE DEPLOYMENT
    # readonly_fields = ('voted',)
