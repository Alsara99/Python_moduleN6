from django.views.generic import DetailView, ListView, TemplateView
from .models import Product


class ProductsListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"
