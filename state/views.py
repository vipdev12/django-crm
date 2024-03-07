from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from state.models import Flat, Category, Manager


# Create your views here.
def home(request):
    return render(request, 'base.html', {})


class FlatList(ListView):
    model = Flat
    context_object_name = 'flats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the category queryset and add it to the context
        context['cats'] = Category.objects.all()

        return context


class FlatCategoryDetail(DetailView):
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')

        # Fetch the category queryset and add it to the context
        context['flats'] = Flat.objects.filter(category_id=pk)
        context['cats'] = Category.objects.all()

        return context


class FlatCreate(CreateView):
    model = Flat
    template_name = 'flat_create.html'
    fields = ['number', 'category', 'floor',
              'square', 'status', 'price',
              'client', 'flat_status']
    success_url = '/flats/'


class FlatUpdate(UpdateView):
    model = Flat
    fields = ['client', 'client_number', 'contract_number']  # Fields to be updated in the form
    template_name = 'flat_update.html'  # Your template for flat update
    success_url = '/flats/'  # URL to redirect after successful update


class FlatDelete(DeleteView):
    model = Flat
    template_name = 'flat_confirm_delete.html'
    success_url = '/flats/'


class ManagerList(ListView):
    model = Manager
    context_object_name = 'managers'


class ManagerCreate(CreateView):
    model = Manager
    template_name = 'manager_create.html'
    fields = ['name', 'phone_number', 'email',
              'quantity_sell', 'password']
    success_url = '/managers/'


class ManagerUpdate(UpdateView):
    model = Manager
    fields = ['name', 'phone_number', 'email', 'password']  # Fields to be updated in the form
    template_name = 'manager_update.html'  # Your template for flat update
    success_url = '/managers/'  # URL to redirect after successful update


class ManagerDelete(DeleteView):
    model = Manager
    template_name = 'manager_confirm_delete.html'
    success_url = '/managers/'
