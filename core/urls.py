from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from .chatbot import chat_with_gemini
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url=reverse_lazy('home')), name='register'),
    path('api/chat/', chat_with_gemini, name='chat_api'),
    path('search/', views.search_flights, name='search'),
    path('feedback/', views.send_feedback, name='feedback'),
    path('generator/', views.web_generator_page, name='web_generator'),
    path('api/generate-web/', views.api_generate_web, name='api_generate_web'),
]