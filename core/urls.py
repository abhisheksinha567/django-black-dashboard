"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django_browser_reload import urls as browser_reload_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('api/auth/', include('dj_rest_auth.urls')),  # Include dj-rest-auth URLs
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Include registration URLs
    path('', include('home.urls')),  # Your app's URLs
    path("__reload__/", include(browser_reload_urls)),  # Include django_browser_reload URLs
]

