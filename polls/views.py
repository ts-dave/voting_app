from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import F
from django.views import View
from .models import Category, Candidate

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')

class CategoryView(LoginRequiredMixin, View):
    def get(self, request, category):
        user = get_user_model().objects.get(username=request.user.username)
        if category in user.voted.split():
            return redirect('polls:result', category=category)

        if category == 'Vice':
            category = 'Vice President'
        user = get_user_model().objects.get(username=request.user.username)
        category = Category.objects.get(category_name=category)
        candidates = category.candidate_set.all()
        context = {
            'candidates': candidates,
            'category': category,
        }
        return render(request, 'vote.html', context)

class VoteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = get_user_model().objects.get(username=request.user.username)
        candidate = get_object_or_404(Candidate, pk=pk)
        candidate.num_of_votes = F('num_of_votes') + 1
        candidate.save()
        candidate.refresh_from_db()
        category = candidate.category
        if category.category_name == 'Vice President':
            user.voted = user.voted + ' ' + 'Vice'
            user.save()
        else:
            user.voted = user.voted + ' ' + category.category_name
            user.save()
        return redirect('polls:result', category=category)

class ResultView(LoginRequiredMixin, View):
    def get(self, request, category):
        if category == 'Vice':
            category = 'Vice President'
        category = Category.objects.get(category_name=category)
        candidates = category.candidate_set.all()
        context = {
            'candidates': candidates,
            'category': category,
        }
        return render(request, 'results.html', context)


class ModalView(LoginRequiredMixin, View):
    def get(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)
        link = f'/vote/{candidate.pk}'
        data = {
            'name': candidate.name,
            'image': candidate.image.url,
            'link': link,
        }
        return JsonResponse(data)
