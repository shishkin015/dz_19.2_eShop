from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
