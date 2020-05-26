from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost



def blog_post_detail(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog_post_detail.html'
	context = {'object':obj}
	return render(request, template, context)




def blog_list_view(request):
	# Add search functionality
	return


def blog_create_view(request):
	return


def blog_retrieve_view(request):
	return


def blog_update_view(request):
	return


def blog_delete_view(request):
	return