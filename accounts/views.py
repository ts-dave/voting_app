from django.shortcuts import render, HttpResponse
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):
        pass
