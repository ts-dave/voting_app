from django.contrib import admin
from .models import Candidate, Category, Vote


class CandidateInline(admin.StackedInline):
    model = Candidate


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    inlines = [CandidateInline]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'num_of_votes']
    # TODO: MAKE num_of_votes FIELD READONLY BEFOR DEPLOYMENT
    # readonly_fields = ('num_of_votes',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'category']
