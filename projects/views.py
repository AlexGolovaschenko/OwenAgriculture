from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from projects.models import ProjectArticle


def projects_list(request):
	try:
		li = get_list_or_404(ProjectArticle)
	except Http404:
		li = []
	context = {'projects_list' : li}
	return render(request, 'projects/projects_list.html', context)


def project_detail(request, id):
	pr = get_object_or_404(ProjectArticle, pk = id)
	context = {'project': pr}
	return render(reques, 'projects/project_detail.html', context)