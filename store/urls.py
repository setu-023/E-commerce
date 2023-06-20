from django.urls import path

from . import views
# from .api import views as api 

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('single-product/<int:pk>', views.single_product, name="single_product"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	# path('api/products', api.ProductList.as_view(), name="product_list"),

]