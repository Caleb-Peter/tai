from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=60)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_image = models.ImageField(null=True, blank=True, upload_to="images/")
	body = models.TextField()
	pub_date = models.DateField(auto_now_add=True)


	def __str__(self):
		return self.title + '~' + str(self.author)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
