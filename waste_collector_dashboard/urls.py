from django.urls import path
from . import views

app_name = 'waste_collector'

urlpatterns = [
    path('dashboard/',views.dashboard, name='waste_collector_dashboard'),

    path('list/', views.collection_list, name='waste_collect_list'),
    path('create/', views.collection_create, name='waste_collect_create'),
    path('update/<int:pk>/', views.collection_update, name='waste_collect_update'),
    path('delete/<int:pk>/', views.collection_delete, name='waste_collect_delete'),

    path('assigned-customers/', views.assigned_waste_customers, name='assigned_customers'),

]