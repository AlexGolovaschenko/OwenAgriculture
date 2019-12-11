from django.shortcuts import render
from django.http import Http404
from products.models import ProductTopic, Product, ProductSpecification

# industry names
PIGSTY = 'pigsty'
POULTRY = 'poultry'


def poultry_catalog(request):
	context = _catalog_context_filter(POULTRY)
	return render(request, 'products/catalog.html', context)


def pigsty_catalog(request):
	context = _catalog_context_filter(PIGSTY)
	return render(request, 'products/catalog.html', context)


def _catalog_context_filter(used_in):
	''' 
	Make a page context dictionary filtered by industry
	Returns a context dictionary including a list of topics and a dictionary with them items
	'''

	# get all topics
	all_topics = ProductTopic.objects.order_by('order')

	# get all items in topics with filter by industry
	items = {}
	for topic in all_topics:
		if used_in == PIGSTY:
			items[topic.headline] = topic.product_set.filter(used_in_pigsty = True)
			title = 'Свиноводство'
		elif used_in == POULTRY:
			items[topic.headline] = topic.product_set.filter(used_in_poultry = True)
			title = 'Птицеводство'

	# remove all empty topics
	topics = []
	for t in all_topics:
		if items[t.headline] :
			topics.append(t)

	# return page context
	return {'topics': topics, 'items': items, 'title': title}


def product_detail(request, id):
	try:
		product = Product.objects.get(id = id)
	except:
		raise Http404("Продукт не найден")	

	if hasattr(product, 'productspecification'):
		spec = product.productspecification
	else:
		spec = []

	context = {'product': product, 'spec': spec}
	return render(request, 'products/product_detail.html', context)