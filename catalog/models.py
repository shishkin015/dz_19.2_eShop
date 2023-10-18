from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    product_description = models.TextField(verbose_name='описание продукта')
    product_preview = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    product_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.product_preview} {self.product_category}' \
               f'{self.product_price} {self.creation_date} {self.last_modified_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Category(models.Model):
    сategory_name = models.CharField(max_length=50, verbose_name='наименование категории')
    сategory_description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.сategory_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('сategory_name',)
