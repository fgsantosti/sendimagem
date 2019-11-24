from django.shortcuts import render
from .models import Post

import numpy as np
import matplotlib.pyplot as plt
# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts':posts})

def view_imgs(request):
	return render(request, 'blog/view_imgs.html',{})

def create_graph():
	# Make a fake dataset:
	height = [3, 12, 5, 18, 45]
	bars = ('A', 'B', 'C', 'D', 'E')
	y_pos = np.arange(len(bars))
	 
	# Create bars
	plt.bar(y_pos, height)
	 
	# Create names on the x-axis
	plt.xticks(y_pos, bars)
	
	plt.savefig('blog/static/blog/img/img_graph.png')
	#plt.savefig('line_plot.pdf')
	#plt.savefig('line_plot.png')  
	#plt.savefig('line_plot.jpg')  

	# Show graphic
	#plt.show()

def view_graph(request):
	create_graph() # chamando o grapha

	return render(request, 'blog/view_graph.html',{})

