from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    anonymous_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='анонимный пользователь')

    def __str__(self):
        return f'{self.name} {self.purchase_price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', null=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Possibilities(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'возможность'
        verbose_name_plural = 'возможности'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.TextField(verbose_name='номер версии')
    name_version = models.CharField(max_length=50, verbose_name='название версии', unique=True)
    indicator = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версия'
