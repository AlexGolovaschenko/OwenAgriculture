from django.shortcuts import render
from django.http import Http404
from products.models import ProductTopic, Product

def poultry_catalog(request):
	topics = ProductTopic.objects.order_by('order')
	items = {}
	for topic in topics:
		items[topic.headline] = topic.product_set.order_by('name')[:16] 

	context = {'topics': topics, 'items': items}

	return render(request, 'products/catalog.html', context)


def pigsty_catalog(request):
	return render(request, 'products/catalog.html')


def product_detail(request, id):
	try:
		product = Product.objects.get(id = id)
	except:
		raise Http404("Продукт не найден")	
	
	context = {'product' : product}
	return render(request, 'products/product_detail.html', context)