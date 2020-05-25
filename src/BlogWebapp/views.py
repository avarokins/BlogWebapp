from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	context = {'title':'Home Page',
				'my_list':[1,2,3,4,5]}
	return render( request,'home.html', context )


def about_page(request):
	return render( request,'about.html', {'title':'About us'} )


def contact_page(request):
	return render( request,'hello_world.html', {'title':'Contact us'} )


def example_page(request):
	context = {'title':'Example title'}
	template_name = 'base.html'
	template_object = get_template(template_name)
	return HttpResponse(template_object.render(context))
