from django.urls import path
from . import views  # Import your views module here

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='store_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('size/<str:size_slug>/', views.store, name='store_by_size'),
    
    #path('price_filter/', views.your_backend_view_name, name='price_filter_view'),
]
