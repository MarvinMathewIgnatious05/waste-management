from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name='customer'

urlpatterns = [

    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),

    path('waste/success/', TemplateView.as_view(template_name="waste_success.html"), name='waste_success'),

    path("list/", views.waste_profile_list, name="waste_profile_list"),
    path("create/", views.waste_profile_create, name="waste_profile_create"),
    path("detail/<int:pk>/", views.waste_profile_detail, name="waste_profile_detail"),
    path("update/<int:pk>/", views.waste_profile_update, name="waste_profile_update"),
    path("delete/<int:pk>/", views.waste_profile_delete, name="waste_profile_delete"),
    path("available_dates/<int:localbody_id>/", views.get_available_dates, name="get_available_dates"),

    path("load_districts/<int:state_id>/", views.load_districts_customer, name="load_districts_customer"),
    path("load_localbodies/<int:district_id>/", views.load_localbodies_customer, name="load_localbodies_customer"),

]
