from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from my_shop.forms import ImageForm

from . import forms
from . import models
from .forms import ImageForm


def index(request):
    return render(request, 'my_shop/index.html')

def get_all_products(request):
    products = models.Product.objects.all()
    return render(request, 'my_shop/products.html', {'products': products})


def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.amount = form.cleaned_data['amount']
        product.image = image
        product.save()
        return redirect('products')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'image': product.image})

    return render(request, 'my_shop/change_product.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) # request.POST чтобы получить текстовую информацию , request.FILES чтобы получить байты
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()  # FileSystemStorage экземпляр позволяет работать с файлами
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'my_shop/upload_image.html', {'form': form})

# def shopping_cart(request, user_id):
#     products = []
#     user = User.objects.filter(pk=user_id).first()
#     orders = Order.objects.filter(customer=user).all()
#     for order in orders:
#         products.append(order.products.all())
#     products.reverse()
#     return render(request, 'my_shop/user_all_orders.html', {'user': user, 'orders': orders, 'products': products})
#
#
# def sorted_shopping_cart(request, user_id, days_ago):
#     products = []
#     product_set = []
#     now = datetime.now()
#     before = now - timedelta(days=days_ago)
#     user = User.objects.filter(pk=user_id).first()
#     orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
#     for order in orders:
#         products = order.products.all()
#         for product in products:
#             if product not in product_set:
#                 product_set.append(product)
#
#     return render(request, 'my_shop/user_all_product.html',
#                   {'user': user, 'product_set': product_set, 'days': days_ago})
