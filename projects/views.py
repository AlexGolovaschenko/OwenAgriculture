from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from projects.models import ProjectArticle


def projects_list(request):
	try:
		li = ProjectArticle.objects.filter(display=True).order_by('-id')
	except:
		li = []

	context = {'projects_list':li}
	return render(request, 'projects/projects_home.html', context)


def project_detail(request, id):
	pr = get_object_or_404(ProjectArticle, pk = id)
	context = {'project': pr}
	return render(request, 'projects/project_detail.html', context)