from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductsListViewByCategory(ListView):
    model = Product
    template_name = "products_by_category.html"
    context_object_name = "products"


    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.object.id
        # Добавляем в контекст полное имя, средний балл и статус сдачи предмета
        context['full_name'] = StudentService.get_full_name(student_id)
        context['average_grade'] = StudentService.calculate_average_grade(student_id)
        context['has_passed'] = StudentService.has_passed(student_id)
        return context


class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"


@method_decorator(cache_page(60 * 15), name='dispatch')
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

