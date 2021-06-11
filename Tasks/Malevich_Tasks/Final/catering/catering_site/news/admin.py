from django.contrib import admin
from .models import Product, CategoryProduct, News, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'weight', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published','category')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published','category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
