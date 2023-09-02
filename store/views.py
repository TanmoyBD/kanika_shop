from django.shortcuts import render, get_object_or_404
from .models import Product
from size.models import Produt_size
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 2)
        product_page = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 4)
        product_page = paginator.get_page(page)
    categories = Category.objects.all()
    size = Produt_size.objects.all()
    context = {"products": product_page, "categories": categories, "size": size }
    return render(request, "store.html", context)



def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    print(product.id)

    return render(request, "product_detail.html", {'product':product})