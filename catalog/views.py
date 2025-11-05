from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView
)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import get_products_from_cache


class ProductListView(ListView):
    """Общедоступный список товаров"""
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


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
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание товара - только для авторизованных"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_create')

    def form_valid(self, form):
        """Автоматически присваивает владельца при создании"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Обновление информации о товаре - только для владельца продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        """Проверка, что пользователь — владелец или суперпользователь"""
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.is_superuser

    def handle_no_permission(self):
        raise PermissionDenied("Вы не можете редактировать этот продукт")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта - только для модератора и владельца"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user

        if user == product.owner or user.is_superuser or user.has_perm('catalog.can_delete_product'):
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("Вы не можете удалить этот продукт.")
