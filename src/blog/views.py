from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost


def blog_list_view(request):
	# Add search functionality
	template = 'blog_post_list.html'
	context = {'object_list':[]}
	return


def blog_create_view(request):
	template = 'blog_post_create.html'
	context = {'form':None}
	return


def blog_detail_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog_post_detail.html'
	context = {'object':obj}
	return


def blog_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog_post_update.html'
	context = {'object':obj,
				'form':None}


	return


def blog_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog_post_delete.html'
	context = {'object':obj}


	return