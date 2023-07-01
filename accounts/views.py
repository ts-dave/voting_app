from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views import View


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('polls:home')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:home')
        else:
            return redirect('accounts:login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
