from django.shortcuts import render, get_object_or_404
from store.models import *



def index(request):
    product = Product.objects.all()[:8]

    context ={
        'product': product,
    }

    return render(request, "web/index.html",context=context)

def single_product(request, id):
    product = get_object_or_404(Product, id=id)

    # Fetch related products (same category, excluding the current product)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    # Fetch reviews for the product
    # reviews = Product.reviews.all()

    return render(request, 'web/single_product.html', {
        'product': product,
        'related_products': related_products,
        # 'reviews': reviews
    })

def all_products(request):

    product = Product.objects.all()
   
    return render(request, 'web/all_products.html', {
            'product': product,

        })
