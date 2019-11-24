from django.urls import path
from . import views #trazendo a biblioteca views.py

from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path
from django.views.static import serve

urlpatterns = [
	path('', views.view_imgs, name='view_imgs'),
	path('view_graph', views.view_graph, name='view_graph'),
	path('post_list', views.post_list, name='post_list'),
]

