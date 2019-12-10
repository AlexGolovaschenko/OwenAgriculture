from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
	path('', views.projects_list, name='projects_list'),
    path('<int:id>/', views.project_detail, name='project_detail'),
]