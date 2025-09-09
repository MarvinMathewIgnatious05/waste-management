from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from authentication.models import CustomUser
from waste_collector_dashboard.models import WasteCollection
from customer_dashboard.models import CustomerWasteInfo
from django.contrib import messages


@login_required
def admin_home(request):
    return render(request, 'super_admin_dashboard.html')




def user_list_view(request):
    customers = CustomUser.objects.filter(role=0)
    collectors = CustomUser.objects.filter(role=1)
    admins = CustomUser.objects.filter(role=2)

    return render(request, 'user_list.html', {
        'customers': customers,
        'collectors': collectors,
        'admins': admins,
    })

def view_customers(request):
    customers = CustomUser.objects.filter(role=0)
    return render(request, 'view_customers.html', {'customers': customers})


def view_waste_collectors(request):
    collectors = CustomUser.objects.filter(role=1)
    total_collectors = collectors.count()
    return render(request, 'view_collectors.html', {'collectors': collectors, 'total_collectors': total_collectors})

def view_super_admin(request):
    super_admin = CustomUser.objects.filter(role=2)
    return render(request, "view_super_admin.html", {"super_admin":super_admin})

def view_admins(request):
    admins = CustomUser.objects.filter(role=3)
    return render(request, "view_admins.html", {"admins":admins})

# \\\\\\\\\\\\\\\\\\\\\\\\\\\ user view //////////////////////

from .forms import UserForm


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, "users_list.html", {"users": users})

# Create new user
# def user_create(request):
#     if request.method == "POST":
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User created successfully")
#             return redirect("super_admin_dashboard:users_list")
#     else:
#         form = UserForm()
#     return render(request, "user_form.html", {"form": form})
#
# # Update user
# def user_update(request, user_id):
#     user = get_object_or_404(CustomUser, id=user_id)
#     if request.method == "POST":
#         form = UserForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User updated successfully")
#             return redirect("super_admin_dashboard:user_list")
#     else:
#         form = UserForm(instance=user)
#     return render(request, "user_form.html", {"form": form})





def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:  # Encrypt password before saving
                user.set_password(password)
            else:  # Default password if none provided
                user.set_password("default123")
            user.save()
            return redirect('super_admin_dashboard:users_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# Update User
def user_update(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:  # Reset password if admin entered new one
                user.set_password(password)
            user.save()
            return redirect('super_admin_dashboard:users_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'user': user})






# Delete user
def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect("super_admin_dashboard:users_list")
    return render(request, "user_confirm_delete.html", {"user": user})




#customerwasteinfoview
#adminassigntowastecollector

# View all CustomerWasteInfo entries
def view_customer_wasteinfo(request):
    waste_infos = CustomerWasteInfo.objects.all()
    collectors = CustomUser.objects.filter(role=1)
    return render(request, 'view_customer_wasteinfo.html', {
        'waste_infos': waste_infos,
        'collectors': collectors,
    })


# Assign a waste collector to a CustomerWasteInfo entry
def assign_waste_collector(request, pk):
    waste_info = get_object_or_404(CustomerWasteInfo, pk=pk)
    if request.method == 'POST':
        collector_id = request.POST.get('collector')
        collector = get_object_or_404(CustomUser, pk=collector_id, role=1)
        waste_info.assigned_collector = collector
        waste_info.save()
        messages.success(request, "Assigned to collector successfully.")
        return redirect('super_admin_dashboard:view_customer_waste_info')
    collectors = CustomUser.objects.filter(role=1)
    return render(request, 'assign_waste_collector.html', {
        'waste_info': waste_info,
        'collectors': collectors,
    })


#waste collector collect details from customer



def view_collected_data(request):
    all_data = WasteCollection.objects.all()
    return render(request, 'view_collected_data.html', {
        'all_data': all_data
    })













# def map_role(request, user_id):
#     user = get_object_or_404(CustomUser, id=user_id)
#     if request.method == "POST":
#         new_role = request.POST.get("role")
#         if new_role in dict(CustomUser.ROLE_CHOICES).keys():
#             user.role = int(new_role)
#             user.save()
#             return redirect("super_admin_dashboard:users_list")
#     return render(request, "map_role.html", {"user": user, "roles": CustomUser.ROLE_CHOICES})




def map_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        new_role = request.POST.get("role")
        if new_role is not None:
            try:
                new_role = int(new_role)  # Convert string to int
                if new_role in dict(CustomUser.ROLE_CHOICES).keys():
                    user.role = new_role
                    user.save()
                    return redirect("super_admin_dashboard:users_list")
            except ValueError:
                pass  # Ignore invalid input
    return render(request, "map_role.html", {"user": user, "roles": CustomUser.ROLE_CHOICES})
