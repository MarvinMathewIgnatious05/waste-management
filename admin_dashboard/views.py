from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from authentication.models import CustomUser
from waste_collector_dashboard.models import WasteCollection
from customer_dashboard.models import CustomerWasteInfo
from django.contrib import messages


@login_required
def admin_home(request):
    return render(request, 'admin_dashboard.html')




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
    return render(request, 'view_collectors.html', {'collectors': collectors})

def view_admins(request):
    admins = CustomUser.objects.filter(role=2)
    return render(request, "view_admins.html", {"admins":admins})




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
        return redirect('admin_dashboard:view_customer_waste_info')
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