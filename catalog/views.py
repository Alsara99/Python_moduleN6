from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, template_name="home.html", context=context)


def contacts(request):
    return render(request, template_name="contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, template_name="product.html", context=context)