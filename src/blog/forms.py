from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title','slug','content','publish_date']

	def title_cleaning(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact=title)
		if self.instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError('This title is already in use. Use another one.')
		return title