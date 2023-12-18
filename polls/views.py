from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import F
from django.views import View
from .models import Category, Candidate, Vote


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "index.html")


class CategoryView(LoginRequiredMixin, View):

    def get(self, request, category):
        if category == "Vice":
            category = "Vice President"

        user = get_user_model().objects.get(username=request.user.username)
        category = Category.objects.get(category_name=category)

        if Vote.objects.filter(voter=user, category=category).first():
            return redirect("polls:result", category=category)

        candidates = category.candidate_set.all()
        context = {
            "candidates": candidates,
            "category": category,
        }
        return render(request, "vote.html", context)


class VoteView(LoginRequiredMixin, View):
    def get(self, request, pk):

        user = get_user_model().objects.get(username=request.user.username)
        candidate = get_object_or_404(Candidate, pk=pk)

        if Vote.objects.filter(voter=user, category=candidate.category).first():
            messages.error(request, "You have already voted for this category! You can't vote twice")
            return redirect("polls:result", category=candidate.category)

        candidate.num_of_votes = F("num_of_votes") + 1
        candidate.save()
        candidate.refresh_from_db()
        Vote.objects.create(voter=user, category=candidate.category)
        messages.success(request, "You have successfuly voted for this category!")
        return redirect("polls:result", category=candidate.category)


class ResultView(LoginRequiredMixin, View):
    def get(self, request, category):

        if category == "Vice":
            category = "Vice President"

        category = Category.objects.get(category_name=category)
        candidates = category.candidate_set.all()
        context = {
            "candidates": candidates,
            "category": category,
        }
        return render(request, "results.html", context)


class ModalView(LoginRequiredMixin, View):
    def get(self, request, pk):
        candidate = get_object_or_404(Candidate, pk=pk)

        link = f"/vote/{candidate.pk}"
        data = {
            "name": candidate.name,
            "image": candidate.image.url,
            "link": link,
        }
        return JsonResponse(data)
