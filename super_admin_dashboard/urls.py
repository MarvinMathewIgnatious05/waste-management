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



    #CALENDAR

    path("calendar/", views.calendar_view, name="calendar"),
    path("calendar/districts/<int:state_id>/", views.load_districts, name="load_districts"),
    path("calendar/localbodies/<int:district_id>/", views.load_localbodies, name="load_localbodies"),
    path("calendar/events/<int:localbody_id>/", views.get_calendar_dates, name="get_calendar_dates"),

    path("calendar/create/<int:localbody_id>/", views.create_calendar_date, name="create_calendar_date"),
    path("calendar/update/<int:pk>/", views.update_calendar_date, name="update_calendar_date"),
    path("calendar/delete/<int:pk>/", views.delete_calendar_date, name="delete_calendar_date"),

#create oder
    path("create-waste-profile/", views.create_waste_profile, name="create_waste_profile"),







]
