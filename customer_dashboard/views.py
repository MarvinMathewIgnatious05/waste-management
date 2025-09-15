
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET
from .models import CustomerWasteInfo, CustomerPickupDate
from super_admin_dashboard.models import State, District, LocalBody, LocalBodyCalendar
from .utils import is_customer


# role checking
class CustomerRoleRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 0




@login_required
def customer_dashboard(request):
    if request.user.role != 0:
        return redirect('authentication:login')
    return render(request, 'customer_dashboard.html')






@login_required
@user_passes_test(is_customer)
def waste_profile_list(request):
    profiles = CustomerWasteInfo.objects.filter(user=request.user)
    return render(request, "waste_profile_list.html", {"profiles": profiles})


@login_required
@user_passes_test(is_customer)
def waste_profile_detail(request, pk):
    info = get_object_or_404(CustomerWasteInfo, pk=pk, user=request.user)
    selected_dates = CustomerPickupDate.objects.filter(user=request.user).values_list("localbody_calendar__date", flat=True)
    return render(request, "waste_profile_detail.html", {"info": info, "selected_dates": selected_dates})




@login_required
@user_passes_test(lambda u: u.role == 0)
def waste_profile_create(request):
    states = State.objects.all()
    ward_range = range(1, 16)
    bag_range = range(1, 11)

    if request.method == "POST":
        info = CustomerWasteInfo.objects.create(
            user=request.user,
            full_name=request.POST.get("full_name"),
            secondary_number=request.POST.get("secondary_number"),
            pickup_address=request.POST.get("pickup_address"),
            landmark=request.POST.get("landmark"),
            state_id=request.POST.get("state"),
            district_id=request.POST.get("district"),
            localbody_id=request.POST.get("localbody"),
            ward=request.POST.get("ward"),
            number_of_bags=request.POST.get("number_of_bags"),
            waste_type=request.POST.get("waste_type"),
            comments=request.POST.get("comments"),
            pincode=request.POST.get("pincode")
        )

        selected_date_id = request.POST.get("selected_date")
        if selected_date_id:
            try:
                cal = LocalBodyCalendar.objects.get(pk=int(selected_date_id))
                CustomerPickupDate.objects.create(
                    user=request.user,
                    waste_info=info,
                    localbody_calendar=cal
                )
            except LocalBodyCalendar.DoesNotExist:
                pass

        return render(request, "waste_success.html", {"info": info})

    return render(request, "waste_form.html", {
        "states": states,
        "ward_range": ward_range,
        "bag_range": bag_range,
        "selected_dates": [],
        "districts": [],
        "localbodies": [],
        "info": None,
    })


@login_required
@user_passes_test(lambda u: u.role == 0)
def waste_profile_update(request, pk):
    info = get_object_or_404(CustomerWasteInfo, pk=pk, user=request.user)
    states = State.objects.all()
    ward_range = range(1, 16)
    bag_range = range(1, 11)

    # Preload districts & localbodies for the selected state/district
    districts = District.objects.filter(state=info.state) if info.state else []
    localbodies = LocalBody.objects.filter(district=info.district) if info.district else []

    # Preload existing selected dates
    selected_dates = CustomerPickupDate.objects.filter(waste_info=info)

    if request.method == "POST":
        # Update main waste info
        info.full_name = request.POST.get("full_name")
        info.secondary_number = request.POST.get("secondary_number")
        info.pickup_address = request.POST.get("pickup_address")
        info.landmark = request.POST.get("landmark")
        info.state_id = request.POST.get("state")
        info.district_id = request.POST.get("district")
        info.localbody_id = request.POST.get("localbody")
        info.ward = request.POST.get("ward")
        info.number_of_bags = request.POST.get("number_of_bags")
        info.waste_type = request.POST.get("waste_type")
        info.comments = request.POST.get("comments")
        info.pincode = request.POST.get("pincode")
        info.save()

        # Handle pickup date update (replace old one with new if given)
        selected_date_id = request.POST.get("selected_date")
        if selected_date_id:
            try:
                cal = LocalBodyCalendar.objects.get(pk=int(selected_date_id))
                # Remove old pickup dates for this profile
                CustomerPickupDate.objects.filter(waste_info=info).delete()
                # Create new pickup date
                CustomerPickupDate.objects.create(
                    user=request.user,
                    waste_info=info,
                    localbody_calendar=cal
                )
            except LocalBodyCalendar.DoesNotExist:
                pass

        return redirect("customer:waste_profile_detail", pk=info.id)

    return render(request, "waste_form.html", {
        "states": states,
        "ward_range": ward_range,
        "bag_range": bag_range,
        "selected_dates": selected_dates,
        "districts": districts,
        "localbodies": localbodies,
        "info": info,
    })


@login_required
@user_passes_test(is_customer)
def waste_profile_delete(request, pk):
    info = get_object_or_404(CustomerWasteInfo, pk=pk, user=request.user)
    if request.method == "POST":
        info.delete()
        return redirect("customer:waste_profile_list")
    return render(request, "waste_profile_delete.html", {"info": info})

def get_available_dates(request, localbody_id):
    all_dates = LocalBodyCalendar.objects.filter(localbody_id=localbody_id)
    data = []
    for d in all_dates:
        data.append({
            "id": d.id,
            "date": d.date.isoformat(),
            "title": "Available",   # always available
        })
    return JsonResponse(data, safe=False)


@login_required
@user_passes_test(is_customer)
@require_GET
def load_districts_customer(request, state_id):
    districts = District.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(districts), safe=False)

@login_required
@user_passes_test(is_customer)
@require_GET
def load_localbodies_customer(request, district_id):
    localbodies = LocalBody.objects.filter(district_id=district_id).values('id', 'name', 'body_type')
    return JsonResponse(list(localbodies), safe=False)


def save_pickup_date(request):
    if request.method == "POST":
        user = request.user
        date_id = request.POST.get("pickup_date")  # This should be LocalBodyCalendar.id
        localbody_calendar = get_object_or_404(LocalBodyCalendar, pk=date_id)

        # Create or update
        CustomerPickupDate.objects.update_or_create(
            user=user,
            defaults={"localbody_calendar": localbody_calendar}
        )
