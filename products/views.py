from django.shortcuts import render

def poultry_catalog(request):
	return render(request, 'products/poultry_catalog.html')

def pigsty_catalog(request):
	return render(request, 'products/pigsty_catalog.html')