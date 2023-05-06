from django.contrib import admin

from apps.task3.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "marja", "package_code")
