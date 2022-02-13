from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from products.models import Product

class HomeViewSitemap(Sitemap):

    def items(self):
        return Product.objects.all().order_by('-created')[:9]
