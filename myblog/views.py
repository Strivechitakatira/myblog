from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

def home(request):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(request, "myblog/home.html", context)

def about(request):
	context = {}
	return render(request, "myblog/about.html", context) 

class PostListView(ListView):
	model = Post
	template_name = 'myblog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	template_name = 'myblog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']