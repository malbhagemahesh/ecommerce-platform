from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cart
from products.models import Product


def add_to_cart(request, product_id):

    user = User.objects.first()

    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart_view(request):

    user = User.objects.first()

    cart_items = Cart.objects.filter(user=user)

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(
        request,
        'cart/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


def remove_from_cart(request, cart_id):

    cart_item = Cart.objects.get(id=cart_id)

    cart_item.delete()

    return redirect('cart')