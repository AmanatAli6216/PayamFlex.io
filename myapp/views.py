from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):

    products = Product.get_all_prodect()
    if request.method =="GET":
        name=request.GET.get("searchname")
        if name!=None:
            products=Product.objects.filter(name__icontains=name)

    return render(request,'index.html', {'products':products})

def contact(request):

    return render(request,'contact.html')