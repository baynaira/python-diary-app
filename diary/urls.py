from django.urls import path
from .views import register_request
from django.contrib.auth.views import LoginView, LogoutView
from .  import views

app_name = 'diary' 

urlpatterns = [
    path('register/', register_request, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='diary:login'), name='logout'), 
    path('', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_create, name='entry_create'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),
]
