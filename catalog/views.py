from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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


class ProductDetailView(DetailView):
    model = Product
    #  catalog/product_detail.html


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_create')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list.html')


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_confirm_delete.html')
