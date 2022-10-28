from django.shortcuts import render

#from inventory.models import Product    #import inventory model to use it here
from django.http import HttpResponse
def home(request):
    #declare a var to use in the front end
    #withing the Product, go thorught all of the objects within the class, filter which one who are in stock only 
    #products = Product.objects.all().filter(is_available=True)


    #context represents what to share from back to end
    #context={
    #    'products_to_front':products,
    #}

    #render to home.html with the contest together
    #return render(request, "home.html", context)
    return render(request, "home.html")