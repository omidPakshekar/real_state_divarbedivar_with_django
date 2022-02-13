from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from .models import Product, Category

class ProductViewSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

class CategoryViewSitemap(Sitemap):
    def items(self):
        return Category.objects.all()
