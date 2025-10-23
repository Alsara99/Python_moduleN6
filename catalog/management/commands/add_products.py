from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()