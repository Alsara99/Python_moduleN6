from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок поста",
        help_text="Введите заголовок поста",
    )
    text = models.TextField(
        verbose_name="Содержимое поста", help_text="Введите содержимое поста"
    )
    image = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    created_at = models.DateField(
        verbose_name="Дата создания товара", help_text="Введите дату создания товара"
    )
    is_posted = models.BooleanField(
        default=False, verbose_name="Статус поста", help_text="Установите статус поста"
    )
    number_of_views = models.IntegerField(
        verbose_name="Количество просмотров", help_text="Введите количество просмотров"
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["name", "if_posted"]

