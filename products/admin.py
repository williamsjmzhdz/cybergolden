from django.contrib import admin
from products.models import *

# Register your models here.ter(CustomUser)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')  


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')  


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'product', 'stock', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')  