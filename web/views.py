from django.shortcuts import render, get_object_or_404
from store.models import *



def index(request):
    product = Product.objects.all()[:6]

    context ={
        'product': product,
    }

    return render(request, "web/index.html",context=context)

def single_product(request, id):
    product = get_object_or_404(Product, id=id)
    

    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    return render(request, 'single_product.html', {
        'product': product,
        'related_products': related_products
    })

