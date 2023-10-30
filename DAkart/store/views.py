from django.shortcuts import get_object_or_404, render
from . models  import Product
from django.db import connection
from category.models import Category

# Create your views here.
def store(request,category_url=None):
    categories = None
    products = None
    print(connection.queries)
    
    if category_url!= None:
        categories = get_object_or_404(Category,url = category_url)
        products =   Product.objects.all().filter(category = categories,is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
       
    product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count
    }
    return render(request,'store.html',context)
     

def product_detail(request,category_url,product_url):
    try:
        single_product = Product.objects.get(category__url=category_url,slug=product_url)
    except Exception as e:
        raise e
    
    context={
        'single_product':single_product
    }
    return render(request,'product-detail.html',context)
