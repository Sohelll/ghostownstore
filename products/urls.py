from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('search', views.search, name='search'),
    path('<int:product_id>', views.product, name='product'),
    path('category/<int:category_id>', views.cat_wise, name='cat_wise'),
    path('checkout_single/<int:product_id>', views.checkout_single, name='checkout_single'),
    path('checkout/<int:user_id>', views.checkout, name='checkout'),
    path('checkout/', views.checkout_tologin, name='checkout_tologin'),

    # Ajax runtime response url, from every page!
    path('ajax/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('checkout/ajax/delete_from_cart', views.delete_from_cart, name='delete_from_cart'),
    path('category/ajax/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('ajax/delete_from_cart', views.delete_from_cart, name='delete_from_cart'),
]
