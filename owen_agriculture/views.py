from django.shortcuts import render

def home(request):
	return render(request, 'owen_agriculture/home.html')

def about(request):
	return render(request, 'owen_agriculture/about_company.html')

def contacts(request):
	return render(request, 'owen_agriculture/contacts.html')

def poultry_home(request):
	return render(request, 'owen_agriculture/poultry_home.html')

def pigsty_home(request):
	return render(request, 'owen_agriculture/pigsty_home.html')

def projects(request):
	return render(request, 'owen_agriculture/projects.html')

def news(request):
	return render(request, 'owen_agriculture/news.html')