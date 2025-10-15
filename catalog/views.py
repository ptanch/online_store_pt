from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    #  catalog/product_list.html


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["success_message"] = "Данные успешно отправлены"
        return self.render_to_response(context)

# def contacts(request):
#     if request.method == 'POST':
#         return render(request, 'contacts.html',{"success_message": "Данные успешно отправлены"})
#     return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    #  catalog/product_detail.html
