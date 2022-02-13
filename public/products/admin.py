from django.contrib import admin
# from django.forms import PositiveIntegerField
from .models import Category, Product
from django.db import models
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # create slug with name
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created']
    list_filter = [ 'created', 'category']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
            models.IntegerField: {'widget': forms.TextInput(attrs={'size':'20'})},
    }


admin.site.register(Product, ProductsAdmin)
