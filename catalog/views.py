from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    #  catalog/product_list.html


def contacts(request):
    if request.method == 'POST':
        return render(request, 'contacts.html',{"success_message": "Данные успешно отправлены"})
    return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    #  catalog/product_detail.html
