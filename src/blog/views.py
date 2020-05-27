from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost


def blog_list_view(request):
	# Add search functionality
	# qs = BlogPost.objects.filter(title__icontains='search_key')
	qs = BlogPost.objects.all()		# queryset
	template = 'blog/list.html'
	context = {'object_list':qs}
	return render(request,template,context)


def blog_create_view(request):
	template = 'blog/create.html'
	context = {'form':None}
	return render(request,template,context)


def blog_detail_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog/detail.html'
	context = {'object':obj}
	return render(request,template,context)


def blog_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog/update.html'
	context = {'object':obj,
				'form':None}


	return render(request,template,context)


def blog_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog/delete.html'
	context = {'object':obj}


	return render(request,template,context)