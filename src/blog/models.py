from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPost(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null = True)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	publishDate = models.DateTimeField(auto_now=False,auto_now_add=False)

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"/blog/{self.slug}/edit"

	def get_delete_url(self):
		return f"/blog/{self.slug}/delete/"
