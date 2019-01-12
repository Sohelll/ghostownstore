from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('search', views.search, name='search'),
    path('<int:product_id>', views.product, name='product'),
    path('category/<int:category_id>', views.cat_wise, name='cat_wise'),
]
