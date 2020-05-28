from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
	qs = BlogPost.objects.all()[:5]
	context = {'title':'Welcome to Saini Blogging!',
				'blog_list':qs}
	return render( request,'home.html', context )


def about_page(request):
	return render( request,'about.html', {'title':'About us'} )


def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		pass
	form = ContactForm()
	context = {
	'title':'Contact us',
	"form":form
	}
	return render( request,'form.html',context  )


def example_page(request):
	context = {'title':'Example title'}
	template_name = 'base.html'
	template_object = get_template(template_name)
	return HttpResponse(template_object.render(context))
