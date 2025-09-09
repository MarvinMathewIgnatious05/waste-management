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
# class WasteInfoCreateView(LoginRequiredMixin, CustomerRoleRequiredMixin, CreateView):
#     model = CustomerWasteInfo
#     form_class = CustomerWasteInfoForm
#     template_name = 'customer_waste_form.html'
#     success_url = reverse_lazy('customer:waste_detail')
#
#     def dispatch(self, request, *args, **kwargs):
#         # Prevent duplicate creation
#         if CustomerWasteInfo.objects.filter(user=request.user).exists():
#             messages.info(request, "You already have a waste profile.")
#             return redirect('customer:waste_detail')
#         return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#

from django.urls import reverse

class WasteInfoCreateView(LoginRequiredMixin, CustomerRoleRequiredMixin, CreateView):
    model = CustomerWasteInfo
    form_class = CustomerWasteInfoForm
    template_name = 'customer_waste_form.html'

    def dispatch(self, request, *args, **kwargs):
        # Prevent duplicate creation
        if CustomerWasteInfo.objects.filter(user=request.user).exists():
            messages.info(request, "You already have a waste profile.")
            return redirect('customer:waste_detail')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # redirect to success page after submission
        return reverse('customer:waste_success')


# Read
# class WasteInfoDetailView(LoginRequiredMixin, CustomerRoleRequiredMixin, DetailView):
#     model = CustomerWasteInfo
#     template_name = 'customer_waste_detail.html'
#
#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = CustomerWasteInfo.objects.get(user=self.request.user)
#             context = self.get_context_data(object=self.object)
#             return self.render_to_response(context)
#         except CustomerWasteInfo.DoesNotExist:
#             return redirect('customer:waste_create')
# #
#


class WasteInfoDetailView(LoginRequiredMixin, CustomerRoleRequiredMixin, DetailView):
    model = CustomerWasteInfo
    template_name = 'customer_waste_detail.html'
    context_object_name = 'waste_info'

    def get_object(self, queryset=None):
        return CustomerWasteInfo.objects.filter(user=self.request.user).first()

    def dispatch(self, request, *args, **kwargs):
        if not CustomerWasteInfo.objects.filter(user=request.user).exists():
            return redirect('customer:waste_create')
        return super().dispatch(request, *args, **kwargs)


# Update
class 	WasteInfoUpdateView(LoginRequiredMixin, CustomerRoleRequiredMixin, UpdateView):
    model = CustomerWasteInfo
    form_class = CustomerWasteInfoForm
    template_name = 'customer_waste_form.html'
    success_url = reverse_lazy('customer:waste_detail')

    def get_object(self):
        return CustomerWasteInfo.objects.get(user=self.request.user)





# Delete
# class WasteInfoDeleteView(LoginRequiredMixin, CustomerRoleRequiredMixin, DeleteView):
#     model = CustomerWasteInfo
#     template_name = 'customer_waste_delete.html'
#     success_url = reverse_lazy('customer:waste_create')
#
#     def get_object(self):
#         return CustomerWasteInfo.objects.get(user=self.request.user)

#
#
class WasteInfoDeleteView(LoginRequiredMixin, CustomerRoleRequiredMixin, DeleteView):
    model = CustomerWasteInfo
    template_name = 'customer_waste_delete.html'
    success_url = reverse_lazy('customer:waste_create')

    def get_object(self, queryset=None):
        return CustomerWasteInfo.objects.filter(user=self.request.user).first()

    def dispatch(self, request, *args, **kwargs):
        if not CustomerWasteInfo.objects.filter(user=request.user).exists():
            messages.warning(request, "No record found to delete.")
            return redirect('customer:waste_create')
        return super().dispatch(request, *args, **kwargs)
#
#
#
#

@login_required
def customer_dashboard(request):
    if request.user.role != 0:
        return redirect('authentication:login')
    return render(request, 'customer_dashboard.html')

#
#
#
#
#
#
#
#













#
#
# # customer_dashboard/views.py
# # from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
# # from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# # from django.urls import reverse_lazy
# # from .models import CustomerWasteInfo
# # from .forms import CustomerWasteInfoForm
# # from django.shortcuts import get_object_or_404, redirect, render
# # from django.contrib import messages
# # from django.contrib.auth.decorators import login_required
# #
# #
# # # Role checking
# # class CustomerRoleRequiredMixin(UserPassesTestMixin):
# #     def test_func(self):
# #         return self.request.user.is_authenticated and getattr(self.request.user, 'role', None) == 0
# #
# #
# #
# #
# # class WasteInfoCreateView(LoginRequiredMixin, CustomerRoleRequiredMixin, CreateView):
# #     model = CustomerWasteInfo
# #     form_class = CustomerWasteInfoForm
# #     template_name = 'customer_waste_form.html'
# #
# #     def get_form_kwargs(self):
# #         kwargs = super().get_form_kwargs()
# #         kwargs['user'] = self.request.user
# #         return kwargs
# #
# #     def form_valid(self, form):
# #         form.instance.user = self.request.user
# #         messages.success(self.request, "Waste profile created successfully.")
# #         return super().form_valid(form)
# #
# #     def get_success_url(self):
# #         return reverse_lazy('customer:waste_detail')
# #
# # # Read
# # class WasteInfoDetailView(LoginRequiredMixin, CustomerRoleRequiredMixin, DetailView):
# #     model = CustomerWasteInfo
# #     template_name = 'customer_waste_detail.html'
# #
# #     def get_object(self, queryset=None):
# #         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
# #
# #
# # # Update
# # class WasteInfoUpdateView(LoginRequiredMixin, CustomerRoleRequiredMixin, UpdateView):
# #     model = CustomerWasteInfo
# #     form_class = CustomerWasteInfoForm
# #     template_name = 'customer_waste_form.html'
# #
# #     def get_form_kwargs(self):
# #         kwargs = super().get_form_kwargs()
# #         kwargs['user'] = self.request.user
# #         return kwargs
# #
# #     def get_object(self):
# #         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
# #
# #     def form_valid(self, form):
# #         messages.success(self.request, "Waste profile updated successfully.")
# #         return super().form_valid(form)
# #
# #     def get_success_url(self):
# #         return reverse_lazy('customer:waste_detail')
# #
# #
# # # Delete
# # class WasteInfoDeleteView(LoginRequiredMixin, CustomerRoleRequiredMixin, DeleteView):
# #     model = CustomerWasteInfo
# #     template_name = 'customer_waste_delete.html'
# #     success_url = reverse_lazy('customer:waste_create')
# #
# #     def get_object(self):
# #         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
# #
# #
# # @login_required
# # def customer_dashboard(request):
# #     if getattr(request.user, 'role', None) != 0:
# #         return redirect('authentication:login')
# #     return render(request, 'customer_dashboard.html')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.urls import reverse_lazy
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
#
# from .models import CustomerWasteInfo
# from .forms import CustomerWasteInfoForm
#
#
# # Role checking
# class CustomerRoleRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return (
#             self.request.user.is_authenticated
#             and getattr(self.request.user, 'role', None) == 0
#         )
#
#
# class WasteInfoCreateView(LoginRequiredMixin, CustomerRoleRequiredMixin, CreateView):
#     model = CustomerWasteInfo
#     form_class = CustomerWasteInfoForm
#     template_name = 'customer_waste_form.html'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # Pass user to form so it can prefill fields
#         kwargs.update({'user': self.request.user})
#         return kwargs
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, "Waste profile created successfully.")
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('customer:waste_detail')
#
#
# class WasteInfoDetailView(LoginRequiredMixin, CustomerRoleRequiredMixin, DetailView):
#     model = CustomerWasteInfo
#     template_name = 'customer_waste_detail.html'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
#
#
# class WasteInfoUpdateView(LoginRequiredMixin, CustomerRoleRequiredMixin, UpdateView):
#     model = CustomerWasteInfo
#     form_class = CustomerWasteInfoForm
#     template_name = 'customer_waste_form.html'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'user': self.request.user})
#         return kwargs
#
#     def get_object(self):
#         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, "Waste profile updated successfully.")
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('customer:waste_detail')
#
#
# class WasteInfoDeleteView(LoginRequiredMixin, CustomerRoleRequiredMixin, DeleteView):
#     model = CustomerWasteInfo
#     template_name = 'customer_waste_delete.html'
#     success_url = reverse_lazy('customer:waste_create')
#
#     def get_object(self):
#         return get_object_or_404(CustomerWasteInfo, user=self.request.user)
#
#
# @login_required
# def customer_dashboard(request):
#     if getattr(request.user, 'role', None) != 0:
#         return redirect('authentication:login')
#     return render(request, 'customer_dashboard.html')
