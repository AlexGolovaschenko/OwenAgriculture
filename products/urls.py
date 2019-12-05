from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
	path('poultry/', views.poultry_catalog, name='poultry_catalog'),
    path('pigsty/', views.pigsty_catalog, name='pigsty_catalog'),
    path('products/<int:id>', views.product_detail, name='product_detail'),
]