from django.db import models


class ProductsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Категорию продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='products_images', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(to=ProductsCategory, on_delete=models.CASCADE, verbose_name='Категория')
    color = models.CharField(max_length=20, null=True, blank=True, verbose_name='Цвет')
    size = models.CharField(max_length=20, null=True, blank=True, verbose_name='Размер')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name} | Количество: {self.quantity} '
