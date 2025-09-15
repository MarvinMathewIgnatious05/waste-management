
from django.contrib import admin
from .models import State, District, LocalBody, LocalBodyCalendar

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    list_filter = ("state",)
    search_fields = ("name",)

@admin.register(LocalBody)
class LocalBodyAdmin(admin.ModelAdmin):
    list_display = ("name", "district", "body_type")
    list_filter = ("district__state", "body_type")
    search_fields = ("name",)

@admin.register(LocalBodyCalendar)
class LocalBodyCalendarAdmin(admin.ModelAdmin):
    list_display = ("localbody", "date")
    list_filter = ("localbody__district__state", "localbody__district", "localbody")
    search_fields = ("localbody__name", )