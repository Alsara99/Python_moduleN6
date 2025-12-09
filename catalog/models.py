from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    is_posted = models.BooleanField(
        default=False, verbose_name="Статус публикации ", help_text="Установите статус публикации"
    )
    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара"
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото товара",
        help_text="Загрузите фотографию товара",
    )
    category = models.CharField(
        max_length=50,
        verbose_name="Категория товара",
        help_text="Введите категорию товара",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку товара",
        help_text="Введите цену за покупку товара",
    )
    owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='products',
        null=True, blank=True
    )
    date_created = models.DateField(
        verbose_name="Дата создания товара", help_text="Введите дату создания товара"
    )
    date_last_changed = models.DateField(
        verbose_name="Дата последнего изменения товара",
        help_text="Введите дату последнего изменения товара",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
