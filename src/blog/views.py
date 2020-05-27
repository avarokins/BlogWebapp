from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_list_view(request):
	# Add search functionality
	# qs = BlogPost.objects.filter(title__icontains='search_key')
	qs = BlogPost.objects.all()		# queryset
	template = 'blog/list.html'
	context = {'object_list':qs}
	return render(request,template,context)


#@login_required
@staff_member_required
def blog_create_view(request):
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm() #reinitialize
	template = 'form.html'
	context = {'form':form}
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