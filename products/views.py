from django.shortcuts import render
from products.models import *

def detail(request, product_id):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    detail = Product.objects.get(id=product_id)
    
    return render(request, 'detail.html', locals())
