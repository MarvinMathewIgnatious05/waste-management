from django.urls import path
from . import views


app_name = 'admin_dashboard'

urlpatterns = [
    path('dashboard/', views.home, name='admin_dashboard'),
]