from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WasteCollection
from .forms import WasteCollectionForm
from authentication.models import CustomUser
import base64
from django.core.files.base import ContentFile
import uuid
from customer_dashboard.models import CustomerWasteInfo



# Check if the user is a waste collector (role 1)
def is_collector(user):
    return user.is_authenticated and user.role == 1


# Waste Collector Dashboard View
@login_required
def dashboard(request):
    if not is_collector(request.user):
        return redirect('authentication:login')

    waste_entries = WasteCollection.objects.filter(collector=request.user)
    return render(request, 'waste_collector_dashboard.html', {'waste_entries': waste_entries})


# List all waste collection records for the logged-in collector
@login_required
def collection_list(request):
    if not is_collector(request.user):
        return redirect('authentication:login')

    collections = WasteCollection.objects.filter(collector=request.user)
    return render(request, 'waste_collect_list.html', {'collections': collections})


def collection_create(request):
    customer_id = request.GET.get('customer_id')

    if request.method == 'POST':
        form = WasteCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.collector = request.user
            instance.total_amount = instance.kg * 50

            # Handle base64 photo
            photo_data = request.POST.get('photo_data')
            if photo_data:
                format, imgstr = photo_data.split(';base64,')
                ext = format.split('/')[-1]
                file_name = f"{uuid.uuid4()}.{ext}"
                instance.photo.save(file_name, ContentFile(base64.b64decode(imgstr)), save=False)

            instance.save()
            return redirect('waste_collector:waste_collector_dashboard')

    else:
        form = WasteCollectionForm()
        if customer_id:
            try:
                customer_info = CustomerWasteInfo.objects.get(id=customer_id)


            except CustomerWasteInfo.DoesNotExist:
                pass

    return render(request, 'waste_collect_form.html', {'form': form})






@login_required
def collection_update(request, pk):
    if not is_collector(request.user):
        return redirect('authentication:login')

    waste = get_object_or_404(WasteCollection, pk=pk, collector=request.user)
    form = WasteCollectionForm(request.POST or None, request.FILES or None, instance=waste)
    if form.is_valid():
        form.save()
        return redirect('waste_collector:waste_collector_dashboard')
    return render(request, 'waste_collect_form.html', {'form': form})





# Delete a waste collection entry
@login_required
def collection_delete(request, pk):
    if not is_collector(request.user):
        return redirect('authentication:login')

    waste = get_object_or_404(WasteCollection, pk=pk, collector=request.user)
    if request.method == 'POST':
        waste.delete()
        return redirect('waste_collector:waste_collector_dashboard')
    return render(request, 'waste_collect_delete.html', {'waste': waste})





@login_required
def assigned_waste_customers(request):
    collector = request.user
    assigned_customers = CustomerWasteInfo.objects.filter(assigned_collector=collector)
    return render(request, 'assigned_customers_details.html', {
        'assigned_customers': assigned_customers
    })