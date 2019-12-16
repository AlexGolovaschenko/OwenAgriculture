from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
	path('', views.news_home, name='news_list'),
    path('<int:id>/', views.news_detail, name='news_detail'),
]