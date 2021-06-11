from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, CategoryProduct, News, Category
from django import forms

def index(request):
    product = Product.objects.all()
    categories = CategoryProduct.objects.all()
    news = News.objects.all()
    categor = Category.objects.all()
    context = {'product': product, 'title': 'Форматы', 'categories': categories, 'news': news, 'title': 'Список новостей', 'categor': categor}
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    product = Product.objects.filter(category_id=category_id)
    categories = CategoryProduct.objects.all()
    category = CategoryProduct.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'product': product, 'categories': categories, 'category': category })

def get_product(request):
    product = Product.objects.all()
    categories = CategoryProduct.objects.all()
    context = {'product': product, 'title': 'Форматы', 'categories': categories}
    return render(request, 'news/category.html', context)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField()
	copy = forms.BooleanField(required = False)