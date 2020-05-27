from django.shortcuts import render
from django.http import Http404
from products.models import ProductTopic, Product, ProductSpecificationField
import sys

# industry names
PIGSTY = 'pigsty'
POULTRY = 'poultry'
FULL = 'full'

def poultry_catalog(request):
	# topic_filter = request.GET.get('topic_filter', '')
	context = _catalog_context_filter(POULTRY)
	return render(request, 'products/catalog.html', context)


def pigsty_catalog(request):
	# topic_filter = request.GET.get('topic_filter', '')	
	context = _catalog_context_filter(PIGSTY)
	return render(request, 'products/catalog.html', context)

def full_catalog(request):
	# topic_filter = request.GET.get('topic_filter', '')
	context = _catalog_context_filter(FULL)
	return render(request, 'products/catalog.html', context)

def _catalog_context_filter(catalog):
	''' 
	Make a page context dictionary filtered by industry
	Returns a context dictionary including a list of topics and a dictionary with them items
	'''

	# get all topics
	all_topics = ProductTopic.objects.order_by('order')

	# get all items in topics with filter by industry
	items = {}
	for topic in all_topics:
		if catalog == PIGSTY:
			items[topic.headline] = topic.product_set.filter(used_in_pigsty = True).order_by('order')
			title = 'Свиноводство'
			cat = 'pigsty'
		elif catalog == POULTRY:
			items[topic.headline] = topic.product_set.filter(used_in_poultry = True).order_by('order')
			title = 'Птицеводство'
			cat = 'poultry'
		elif catalog == FULL:
			items[topic.headline] = topic.product_set.filter()
			title = 'Каталог'
			cat = 'full'		

	# remove all empty topics
	topics = []
	for t in all_topics:
		if items[t.headline] :
			topics.append(t)

	# return just selcted topic items
	# if topic_filter:
	#	sel = topics[topic_filter]
	#	topics = []
	#	topics.append(sel)

	# return page context
	return {'topics': topics, 'items': items, 'title': title, 'catalog':cat }


def product_detail(request, id):
	try:
		product = Product.objects.get(id = id)
	except:
		raise Http404("Продукт не найден")	

	spec = product.productspecificationfield_set.all().order_by('order')
	# print('hello, im here!', spec, file=sys.stderr)
	catalog = request.GET.get('catalog', '')	

	context = {'product': product, 'spec': spec, 'catalog':catalog}
	return render(request, 'products/product_detail.html', context)