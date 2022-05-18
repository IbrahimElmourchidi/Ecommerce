from django.contrib import admin
from .models import Category, Color, Brand, Size, Product, ProductAttribute, Banner


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']


admin.site.register(Category, CategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'color_tag']


admin.site.register(Color, ColorAdmin)

admin.site.register(Brand)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_editable = ['status']


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color', 'price', 'image_tag']


admin.site.register(ProductAttribute, ProductAttributeAdmin)


admin.site.register(Banner)
