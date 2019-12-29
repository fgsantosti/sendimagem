from django.shortcuts import render
from .models import Post


def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts':posts})

def view_imgs(request):
	return render(request, 'blog/view_imgs.html',{})


