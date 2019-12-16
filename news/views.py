from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from news.models import Article


def news_home(request):
	try:
		li = Article.objects.filter().order_by('-id')
	except:
		li = []

	context = {'news_list':li}
	return render(request, 'news/news_home.html', context)


def news_detail(request, id):
	art = get_object_or_404(Article, pk = id)
	context = {'article': art}
	return render(request, 'news/news_detail.html', context)