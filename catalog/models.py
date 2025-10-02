from django.db import models


class Product(models.Model):
    """Класс для представления продукта"""

    name = models.CharField(
        max_length=100, verbose_name='Наименование', help_text='Введите наименование продукта'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание продукта',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='catalog/photo',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото продукта'
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию продукта',
        blank=True,
        null=True,
        related_name="products"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Описание параметров модели"""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']

    def __str__(self):
        return self.name


class Category(models.Model):
    """Класс для представления категории"""

    name = models.CharField(
        max_length=100, verbose_name='Категория', help_text='Введите категорию'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание категории',
        blank=True,
        null=True
    )

    class Meta:
        """Описание параметров модели"""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
