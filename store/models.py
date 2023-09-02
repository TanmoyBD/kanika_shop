from django.db import models

# Create your models here.
from django.db import models
from category.models import Category
from size.models import Produt_size
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    product_size = models.ForeignKey(Produt_size, on_delete=models.CASCADE,blank=False)
    
    def __str__(self):
        return self.product_name
