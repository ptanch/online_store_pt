from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        return render(request, 'contacts.html',{"success_message": "Данные успешно отправлены"})
    return render(request, 'contacts.html')


def product_iphone(request):
    return render(request, 'product_iphone.html')
