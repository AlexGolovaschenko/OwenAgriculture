from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from news.models import Article


def news_list(request):
	try:
		li = get_list_or_404(Article)
	except Http404:
		li = []
	context = {'news_list' : li}
	return render(request, 'news/news_list.html', context)


def news_detail(request, id):
	art = get_object_or_404(Project, pk = id)
	context = {'article': art}
	return render(reques, 'news/news_detail.html', context)