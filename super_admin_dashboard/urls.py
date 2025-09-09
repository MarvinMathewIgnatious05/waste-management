from django.urls import path
from . import views

app_name = 'super_admin_dashboard'
urlpatterns = [
    path('dashboard/', views.admin_home, name='super_admin_dashboard'),


    path('users/', views.user_list, name='users_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/edit/', views.user_update, name='user_update'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),

    path("users/<int:user_id>/map-role/", views.map_role, name="map_role"),


    path('users/', views.user_list_view, name='user_list'),

    path('users/customers/', views.view_customers, name='view_customers'),
    path('users/collectors/', views.view_waste_collectors, name='view_collectors'),
    path('users/super_admins/', views.view_super_admin, name='view_super_admin'),
    path('users/admins/', views.view_admins, name='view_admins'),

    path('waste-info/', views.view_customer_wasteinfo, name='view_customer_waste_info'),
    path('waste-info/assign/<int:pk>/', views.assign_waste_collector, name='assign_waste_collector'),
    path('collected-data/',views.view_collected_data, name='view_collected_data'),


]
