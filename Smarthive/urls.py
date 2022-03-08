"""Smarthive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajit-saigal/dashboard/', include('dashboard.urls')),
    path('ajit-saigal/accounts/', include('accounts.urls')),
    path('ajit-saigal/', include('adminDashboard.urls')),
    path('function/', include('function.urls')),
    path('questions/', include('questions.urls')),
    path('report/', include('report.urls')),
    path('api/', include('api.urls')),
    path('category/', include('category.urls')),
]

admin.site.site_header = 'Smart Hive administration'
