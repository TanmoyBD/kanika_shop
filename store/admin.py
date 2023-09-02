from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'price', 'category', 'stock', 'created_date', 'modified_date', 'is_available', 'display_sizes']

    def display_sizes(self, obj):
        # Define the size field names you want to display
        size_fields = ['size1', 'size2', 'size3', 'size4', 'size5']

        # Get the labels for the selected sizes from SIZE_CHOICES
        sizes = [dict(Product.SIZE_CHOICES).get(getattr(obj, size)) for size in size_fields if getattr(obj, size)]

        # Join the labels with spaces (e.g., "S M L")
        sizes_str = ' '.join(sizes)

        return sizes_str or "N/A"
    
    display_sizes.short_description = 'Available Sizes'

admin.site.register(Product, ProductAdmin)
