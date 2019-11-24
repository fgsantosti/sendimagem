from django.db import models

# Create your models here.
# python -m pip install Pillow

class Post(models.Model):
	"""docstring for Post"""
	titulo = models.CharField(max_length=200, blank=False)
	imagem = models.ImageField(upload_to='blog/media', blank=False)
	data = models.DateField()
	text = models.TextField()
	
	def __str__(self):
		return self.titulo
		