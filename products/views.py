from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def home(request):
    products = Product.objects.all()[:4]

    return render(
        request,
        'products/home.html',
        {'products': products}
    )





def product_list(request):

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(
            name__icontains=query
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'categories': categories,
            'query': query,
            'selected_category': category_id
        }
    )


def product_detail(request, pk):
    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )