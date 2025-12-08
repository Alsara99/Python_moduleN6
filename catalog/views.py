from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
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
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_edit'):
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")

        model = Product
        form_class = ProductForm
        template_name = 'product_form.html'
        success_url = '/catalog/'

        return redirect('catalog')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        product.delete()

        return redirect('catalog')

