from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'is_published', 
                        'actual_price', 'list_date',)
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'tags',
                     'price',)
    list_per_page = 20

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
