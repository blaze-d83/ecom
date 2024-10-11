from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product':product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('product_list')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})
