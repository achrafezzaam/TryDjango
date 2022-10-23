from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
    
#     context = {
#         "title": "Creating new products",
#         "form": form
#     }
#     return render(request,"products/product_create.html",context)

def product_create_view(request):
    my_form = RawProductForm()

    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
    
    context = {
        "title": "Creating new products",
        "form": my_form
    }
    return render(request,"products/product_create.html",context)
    