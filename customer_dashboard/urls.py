from django.urls import path
from .views import (
    WasteInfoCreateView, WasteInfoDetailView,
    WasteInfoUpdateView, WasteInfoDeleteView,customer_dashboard
)

app_name='customer'

urlpatterns = [

    path('dashboard/', customer_dashboard, name='customer_dashboard'),

    path('profile/create/', WasteInfoCreateView.as_view(), name='waste_create'),
    path('profile/', WasteInfoDetailView.as_view(), name='waste_detail'),
    path('profile/update/', WasteInfoUpdateView.as_view(), name='waste_update'),
    path('profile/delete/', WasteInfoDeleteView.as_view(), name='waste_delete'),
]
