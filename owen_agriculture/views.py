from django.shortcuts import render

def home(request):
	return render(request, 'base_with_banner.html')

def about(request):
	return render(request, 'owen_agriculture/about_company.html')

def contacts(request):
	return render(request, 'owen_agriculture/contacts.html')