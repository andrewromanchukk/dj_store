from django.shortcuts import render
from django.http import HttpResponse 
from .forms import *
from products.models import *



 
def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_folding_knives = products_images.filter(product__category_id=1)
    products_images_automatic_knives = products_images.filter(product__category_id=2)
    products_images_fixed_blade_knives = products_images.filter(product__category_id=3)
    products_images_otf_knives = products_images.filter(product__category_id=4)
    products_images_butterfly_knives = products_images.filter(product__category_id=5)
    products_images_spring_assisted_knives = products_images.filter(product__category_id=6)
    products_images_throwing_knives = products_images.filter(product__category_id=7)
    products_images_exclusive_knives = products_images.filter(product__category_id=8)
    products_images_out_the_front_knives = products_images.filter(product__category_id=9)
    products_images_case_knives = products_images.filter(product__category_id=10)
    return render(request, 'index.html', locals())
 