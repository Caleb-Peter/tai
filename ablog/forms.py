from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'post_image', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'post_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}


class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'post_image', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'post_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}