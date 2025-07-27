from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import CustomerWasteInfo
from .forms import CustomerWasteInfoForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# role checking
class CustomerRoleRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 0



# Create
class WasteInfoCreateView(LoginRequiredMixin, CustomerRoleRequiredMixin, CreateView):
    model = CustomerWasteInfo
    form_class = CustomerWasteInfoForm
    template_name = 'customer_waste_form.html'
    success_url = reverse_lazy('customer:waste_detail')

    def dispatch(self, request, *args, **kwargs):
        # Prevent duplicate creation
        if CustomerWasteInfo.objects.filter(user=request.user).exists():
            messages.info(request, "You already have a waste profile.")
            return redirect('customer:waste_detail')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




# Read
class WasteInfoDetailView(LoginRequiredMixin, CustomerRoleRequiredMixin, DetailView):
    model = CustomerWasteInfo
    template_name = 'customer_waste_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = CustomerWasteInfo.objects.get(user=self.request.user)
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except CustomerWasteInfo.DoesNotExist:
            return redirect('customer:waste_create')




# Update
class 	WasteInfoUpdateView(LoginRequiredMixin, CustomerRoleRequiredMixin, UpdateView):
    model = CustomerWasteInfo
    form_class = CustomerWasteInfoForm
    template_name = 'customer_waste_form.html'
    success_url = reverse_lazy('customer:waste_detail')

    def get_object(self):
        return CustomerWasteInfo.objects.get(user=self.request.user)





# Delete
class WasteInfoDeleteView(LoginRequiredMixin, CustomerRoleRequiredMixin, DeleteView):
    model = CustomerWasteInfo
    template_name = 'customer_waste_delete.html'
    success_url = reverse_lazy('customer:waste_create')

    def get_object(self):
        return CustomerWasteInfo.objects.get(user=self.request.user)




@login_required
def customer_dashboard(request):
    if request.user.role != 0:
        return redirect('home')
    return render(request, 'customer_dashboard.html')












