from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductCreateView,
    ContactsView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryView
)

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),

    path('contacts/', ContactsView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
