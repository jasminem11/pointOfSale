from django.shortcuts import render
from .models import Product

# Create your views here.
def inventory(request):
    products=Product.objects.all().filter(is_available=True)

    context={
        "products":products,
    }

    return render(request, 'templates/home.html', context)

#declare funct search 
#filter over product = keyword
#product_count= sproduct .count()
#def search(request):
 #   product_count = product.count() 