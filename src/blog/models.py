from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPostManager(models.Manager):
	def published(self):
		return self.get_queryset().filter(publishDate__lte=timezone.now)


class BlogPost(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null = True)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	publishDate = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = BlogPostManager()

	class Meta:
		ordering=['-publishDate','-updated','-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"/blog/{self.slug}/edit"

	def get_delete_url(self):
		return f"/blog/{self.slug}/delete/"


