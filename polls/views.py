from django.shortcuts import HttpResponse, render, redirect
from django.db.models import F
from django.views import View
from .models import Category, Candidate

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class CategoryView(View):
    def get(self, request, category):
        if category == 'Vice':
            category = 'Vice President'
        category = Category.objects.get(category_name=category)
        candidates = category.candidate_set.all()
        context = {
            'candidates': candidates,
            'category': category,
        }
        return render(request, 'vote.html', context)

class VoteView(View):
    def get(self, request, candidate):
        candidate = Candidate.objects.filter(name=candidate)
        candidate.update(num_of_votes=F('num_of_votes') + 1)
        voted = True
        return render(request, 'vote.html', context)

class ResultView(View):
    def get(self, request, category):
        category = Category.objects.get(category_name=category)
        candidates = category.candidate_set.all()
        context = {
            'candidates': candidates,
            'category': category,
        }
        return render(request, 'results.html', context)
