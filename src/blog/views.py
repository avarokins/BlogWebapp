from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_list_view(request):
	# Add search functionality
	# qs = BlogPost.objects.filter(title__icontains='search_key')
	qs = BlogPost.objects.published()		# queryset
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

@staff_member_required
def blog_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template = 'form.html'
	context = {'form':form, 
				'title':f"Update {obj.title}"}

	return render(request,template,context)

@staff_member_required
def blog_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/blog/")

	context = {'object':obj}

	return render(request,template,context)



































