from django.urls import path
from Product_Module.views import *

urlpatterns = [
    path('popular-products/', PopularProductsView.as_view(), name='popular_products_url'),
    path('product-categorys/', ProductCategoryView.as_view(), name='product_category_url'),
    path('new-products/', NewProductView.as_view(), name='new_product_url'),
    path('buy-count-products/', BuyCountProductView.as_view(), name='buy_count_product_url'),
    path('visit-count-products/', VisitCountProductView.as_view(), name='visit_count_product_url'),
    path('products-with-category/<pk>/', ProductWithCategoryView.as_view(), name='products_with_category_url'),
    path('detail_product/<pk>/', DetailProductView.as_view(), name='detail_product_url'),
]
