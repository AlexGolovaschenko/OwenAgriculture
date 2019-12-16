from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import Http404
from news.models import Article

def home(request):
	try:
		latest_news = Article.objects.filter().order_by('-id')[:5]
	except:
		latest_news = []

	context = {'latest_news':latest_news}
	return render(request, 'owen_agriculture/home.html', context)

def about(request):
	return render(request, 'owen_agriculture/about_company.html')

def contacts(request):
	return render(request, 'owen_agriculture/contacts.html')

def projects(request):
	return render(request, 'owen_agriculture/projects.html')

def news(request):
	return render(request, 'owen_agriculture/news.html')