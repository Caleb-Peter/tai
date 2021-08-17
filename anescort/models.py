from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import datetime, date


MEMBERSHIP_CHOICES = (
	('VIP', 'VIP'),
	('PREMIUM', 'PREMIUM'),
	('NEW', 'NEW'),
)


class Location(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name


class Membership(models.Model):
	name =  models.CharField(max_length=7, choices=MEMBERSHIP_CHOICES, default='New')


	def __str__(self):
		return self.name

class Escort(models.Model):
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
	Image1 = models.ImageField(null=True, blank=True, upload_to="images/")
	Image2 = models.ImageField(null=True, blank=True, upload_to="images/")
	Image3 = models.ImageField(null=True, blank=True, upload_to="images/")
	name = models.CharField(max_length=10)
	age = models.CharField(max_length=2, default='22')
	author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	about_me = models.TextField()
	phone = models.CharField(max_length=14)
	ethnicity = models.CharField(max_length=20)
	orientation = models.CharField(max_length=20)
	location = models.CharField(max_length=40)
	area = models.CharField(max_length=40)
	skin_color = models.CharField(max_length=40)
	hair_color = models.CharField(max_length=40)
	services = models.CharField(max_length=255)
	membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-membership']
	

	def __str__(self):
		return self.name + '~' + str(self.author)

	def get_absolute_url(self):
		return reverse('escort-details', kwargs={'pk': self.pk})


