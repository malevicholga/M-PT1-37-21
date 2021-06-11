from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Наименование')
    category = models.ForeignKey('CategoryProduct', on_delete=models.PROTECT, null=True, verbose_name = 'Категория продуктов') 
    weight = models.IntegerField(verbose_name = 'Bec')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Фото')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

class CategoryProduct(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Наименование категории')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Фото категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['title']

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Наименование') 
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name = 'Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'
        ordering = ['title']