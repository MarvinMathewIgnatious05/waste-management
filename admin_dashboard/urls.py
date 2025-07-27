from django.urls import path
from . import views

app_name = 'admin_dashboard'
urlpatterns = [
    path('dashboard/', views.admin_home, name='admin_dashboard'),


    path('users/', views.user_list_view, name='user_list'),
    path('users/customers/', views.view_customers, name='view_customers'),
    path('users/collectors/', views.view_waste_collectors, name='view_collectors'),
    path('users/admins/', views.view_admins, name="view_admins"),

    path('waste-info/', views.view_customer_wasteinfo, name='view_customer_waste_info'),
    path('waste-info/assign/<int:pk>/', views.assign_waste_collector, name='assign_waste_collector'),
    path('collected-data/',views.view_collected_data, name='view_collected_data'),


]
