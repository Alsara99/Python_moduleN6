from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/catalog/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/catalog/'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = '/catalog/'
