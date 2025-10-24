from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        categories = Category.objects.all()

        categories.delete()
        products.delete()