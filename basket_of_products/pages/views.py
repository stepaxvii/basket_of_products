from django.views.generic import TemplateView, View

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


class AboutView(TemplateView):
    """CBV страницы о проекте."""

    template_name = 'pages/about.html'


class LoginView(View):
    """CBV страницы входа в аккаунт."""

    def get(self, request):
        return render(request, 'loger/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('basket:index')
        return render(
            request,
            'loger/login.html',
            {'error': 'Invalid username or password'}
        )


class LogoutView(View):
    """CBV страницы выхода из аккаунта."""

    def get(self, request):
        logout(request)
        return redirect('pages:about')
