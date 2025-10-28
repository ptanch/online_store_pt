from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView
)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Общедоступный список товаров"""
    model = Product
    #  catalog/product_list.html


class ContactsView(TemplateView):
    """Страница с отображением контактов"""
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Сообщение при отправке данных с помощью формы контактов"""
        context = self.get_context_data(**kwargs)
        context["success_message"] = "Данные успешно отправлены"
        return self.render_to_response(context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Просмотр конкретного товара - только для авторизованных"""
    model = Product
    #  catalog/product_detail.html


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание товара - только для авторизованных"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_create')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление информации о товаре - только для авторизованных"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление товара - только для авторизованных"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
