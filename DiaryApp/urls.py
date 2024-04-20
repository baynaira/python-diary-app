"""
URL configuration for DiaryApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from diary.views import register_request
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls', namespace='diary')),  # Include the diary app URLs with namespace
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^$', RedirectView.as_view(url='/diary/', permanent=True)),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/registration/login'), name='logout'),  # Correct logout path
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   
    
]
