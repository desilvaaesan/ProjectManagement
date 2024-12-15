"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager-dashboard/', views.base_manager, name='manager-dashboard'),
    path('member-dashboard/', views.base_member, name='member-dashboard'),
    path('users/', include('users.urls')),  # Include user app URLs
    path('projects/', admin.site.urls),
    path('notifications/', admin.site.urls),
    path('tasks/', admin.site.urls),
    path('', include('users.urls')),  # Redirect the root URL to the login page
]