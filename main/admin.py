from django.contrib import admin
from .models import Category, Color, Brand, Size, Product, ProductAttribute

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_editable = ['status']


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'color']


admin.site.register(ProductAttribute, ProductAttributeAdmin)
