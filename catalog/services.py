from .models import Product


class ProductService:

    @staticmethod
    def get_category_products(category):
        return Product.objects.filter(category=category)
