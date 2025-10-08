from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        return render(request, 'contacts.html',{"success_message": "Данные успешно отправлены"})
    return render(request, 'contacts.html')


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'extends/product_list.html', context)


def product_iphone(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_iphone.html', context)
