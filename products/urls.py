from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('search', views.search, name='search'),
    path('<int:product_id>', views.product, name='product'),
    path('category/<int:category_id>', views.cat_wise, name='cat_wise'),
    path('ajax/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('checkout/<int:product_id>', views.checkout, name='checkout'),
    path('checkout_single', views.checkout_single, name='checkout_single'),
    path('category/ajax/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('ajax/delete_from_cart', views.delete_from_cart, name='delete_from_cart'),
]
