from django.db import models

# Create your models here.
from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    size1 = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True)
    size2 = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True)
    size3 = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True)
    size4 = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True)
    size5 = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True)

    def __str__(self):
        return self.product_name
