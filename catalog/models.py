from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    product_description = models.TextField(verbose_name='описание продукта')
    product_preview = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}'

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


class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    version_sign = models.BooleanField(choices=VERSION_CHOICES, verbose_name='признак версии')

    def __str__(self):
        return f'{self.product} {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('version_name',)


@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.version_sign:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(version_sign=False)
