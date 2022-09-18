from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views as users_views


urlpatterns = [
    path('index/', views.indexView, name='home-accounts'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path(
        'logout/',
        LogoutView.as_view(
            template_name="registration/logout.html",
        ),
        name="logout"),
    path('admin/', admin.site.urls, name="admin_url"),
    path('register/', users_views.register, name='register'),
    path('delete/<int:id>/', views.delete_userfollow, name='deletedata')

]
