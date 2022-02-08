from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView,name='home-accounts'),
    path('dashboard/', views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/', views.registerView,name='register_url'),
    path('logout/',LogoutView.as_view(template_name="registration/logout.html",),name="logout"),
    path('admin/', admin.site.urls, name="admin_url"),
]