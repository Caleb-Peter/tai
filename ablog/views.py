from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

#def blog(request):
	#return render(request, 'blog/blog.html', {})

class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'
	ordering = ['-pub_date']

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'blog/add_post.html'
	form_class = PostForm

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'blog/update_post.html'
	form_class = UpdatePostForm
	#fields = ('title', 'body')

class DeletePostView(DeleteView):
	model = Post
	template_name = 'blog/delete_post.html'
	success_url = reverse_lazy('blog')

