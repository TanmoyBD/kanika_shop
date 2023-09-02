from django.contrib import admin
from .models import Produt_size
# Register your models here.
# admin.site.register(Category)

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['size']
    
admin.site.register(Produt_size, ProductSizeAdmin)