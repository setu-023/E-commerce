from calendar import c
from itertools import product
from django.shortcuts import render
from .models import *

def store(request):

	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def single_product(request, pk):

	product = Product.objects.get(id=pk)
	context = {'product':product}
	print(product)
	return render(request, 'store/single_product.html', context)



def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		print(customer) 
	context = {'items': items}
	print(context)
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)