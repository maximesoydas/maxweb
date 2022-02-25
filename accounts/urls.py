from unicodedata import name
from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views as users_views
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('index/', views.indexView,name='home-accounts'),
    path('dashboard/', views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    # path('register/', views.registerView,name='register_url'),
    path('logout/',LogoutView.as_view(template_name="registration/logout.html",),name="logout"),
    path('admin/', admin.site.urls, name="admin_url"),
    path('register/',users_views.register, name='register'),
    path('profile/',ProfileListView.as_view(),name="profile-list-view"),
    path('<pk>/', ProfileDetailView.as_view(), name ='profile-detail-view',)
]

