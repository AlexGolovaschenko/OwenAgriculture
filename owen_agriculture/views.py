from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import Http404
from news.models import Article
from projects.models import ProjectArticle
from banners.models import Banner

def home(request):
	try:
		latest_news = Article.objects.filter(display=True).order_by('-pub_date')[:5]
	except:
		latest_news = []

	try:
		latest_projects = ProjectArticle.objects.filter(display=True).order_by('-id')[:5]
	except:
		latest_projects = []

	try:
		banners = Banner.objects.filter(display=True).order_by('order')
	except:
		banners = []	

	context = {'latest_news':latest_news, 'latest_projects':latest_projects, 'banners':banners}
	return render(request, 'owen_agriculture/home.html', context)

def about(request):
	return render(request, 'owen_agriculture/about_company.html')

def contacts(request):
	return render(request, 'owen_agriculture/contacts.html')

def projects(request):
	return render(request, 'owen_agriculture/projects.html')

def news(request):
	return render(request, 'owen_agriculture/news.html')