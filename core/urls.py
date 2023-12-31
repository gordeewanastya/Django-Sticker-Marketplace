from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from core.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
