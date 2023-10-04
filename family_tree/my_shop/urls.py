from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('products/', views.get_all_products, name='products'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
]