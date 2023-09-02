from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None, size_slug=None ):
    category = None
    products = None
    sizeproducts = None
    if size_slug:
        # Assuming you have updated your Product model to have separate size fields (size1, size2, size3, size4, size5)
        size_fields = [f'size{i}' for i in range(1, 6)]
        if size_slug in size_fields:
            products = products.filter(**{size_slug: 'S'})
            
    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 1)
        product_page = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 3)
        product_page = paginator.get_page(page)
    categories = Category.objects.all()
    context = {"products": product_page, "categories": categories, "size_fields": size_fields}
    print(size_fields)
    return render(request, "store.html", context)



def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    print(product.id)

    return render(request, "product_detail.html", {'product':product})




# views.py
from django.shortcuts import render, redirect
from .forms import PriceFilterForm

#def your_backend_view_name(request):
    
            
            

    