from django.contrib import admin
from .models import Candidate, Category


class CandidateInline(admin.StackedInline):
    model = Candidate

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'date']
    inlines = [CandidateInline]

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_of_votes']
    # readonly_fields = ('num_of_votes',)
