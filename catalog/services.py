from .models import Product


class ProductService:

    @staticmethod
    def get_category_products(category):
        products = Product.objects.filter(category=category)
        return products
