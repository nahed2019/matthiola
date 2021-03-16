from django.contrib import admin
from .models import Product, Category, Occasion


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'product_image',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion)
