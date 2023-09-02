from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.urls import reverse
from django.contrib import messages
from category.models import Category
from django.core.paginator import Paginator
from .forms import MyForm
from django.db.models import Q



# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        # Filter products by category if category_slug is provided
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category).order_by('product_name')
    else:
        # No category_slug provided, filter all available products
        products = Product.objects.filter(is_available=True).order_by('product_name')

    # Paginate the products
    page = request.GET.get("page")
    paginator = Paginator(products, 4)
    product_page = paginator.get_page(page)
    categories = Category.objects.all()
    context = {"products": product_page, "categories": categories}
    return render(request, "store.html", context)



from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import MyForm

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product  # Import your Product model here
from .forms import MyForm  # Import your form here

def FilterItems(request):
    products = Product.objects.filter(is_available=True)  # Initialize with an empty queryset
    context = {}
    product_count = 0
    
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            field1_value = form.cleaned_data['field1']
            field2_value = form.cleaned_data['field2']
            
            products = Product.objects.filter(is_available=True, price__range=(field1_value, field2_value))
            product_count = products.count()
        else:
            # Handle form validation errors here if needed
            pass
    else:
        # No form submission via POST, create an empty form
        form = MyForm()

    # Pagination code
    page = request.GET.get("page")
    paginator = Paginator(products, 4)
    product_page = paginator.get_page(page)
    context["products"] = product_page
    context["product_count"] = product_count
    
    return render(request, 'filter_items.html', {'form': form, **context})


def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    print(product.id)

    return render(request, "product_detail.html", {'product':product})

