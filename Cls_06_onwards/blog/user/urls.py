from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView, TemplateView
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('home/', lambda request: render(request, 'user/home.html'), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SignupView.as_view(), name="create_user"),
]