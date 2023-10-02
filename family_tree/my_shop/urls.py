from django.urls import path
from .views import index, shopping_cart, sorted_shopping_cart




urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('user/<int:user_id>/', shopping_cart, name='basket'),
    path('user_sorted/<int:user_id>/<int:days_ago>/', sorted_shopping_cart, name='sorted_shopping_cart'),


]