from django.contrib import admin

from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name
    list_display = ('name', 'slug')
    search_fields = ('name',)  # Allow searching by category name
class ProductAdmin(admin.ModelAdmin):
    # prepopulated_fields = ('category', 'name', 'price', 'stock', 'available')  
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created_at', 'updated_at')
    list_filter = ('category', 'available', 'created_at', 'updated_at')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)