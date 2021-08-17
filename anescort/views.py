from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Escort, Membership
from .forms import EscortForm, EditEscortForm
from django.urls import reverse_lazy
import random 
from random import shuffle
from itertools import chain
from operator import attrgetter



#def home(request):
	#return render(request, 'home.html',{})


#class HomeView(ListView):
	#model = Escort
	#template_name = 'home.html'
	#ordering = ['-membership']

class AddEscortView(CreateView):
	model = Escort
	form_class = EscortForm
	template_name = 'add_escort.html'
	#fields = '__all__'

class EditEscortView(UpdateView):
	model = Escort
	template_name = 'edit_escort.html'
	form_class = EditEscortForm
	

class EscortDetailView(DetailView):
	model = Escort
	template_name = 'escort_details.html'

# Changed the classbased HomeView above to all_escorts function-based view below

def all_escorts(request):
	escorts_list = Escort.objects.all()
	#recent_escort = list(escorts_list)
	#shuffle(recent_escort)
	return render (request, 'home.html', { 'escorts_list': escorts_list})


def LocationView(request, locs):
	location_escorts = Escort.objects.filter(location=locs.replace('-', ' '))
	return render(request, 'locations.html', {'locs': locs.title().replace('-', ' '), 'location_escorts': location_escorts})


class DeleteEscortView(DeleteView):
	model = Escort
	template_name = 'delete_escort.html'
	success_url = reverse_lazy ('home')


def VIPEscortsView(request):
	VIP_Escorts = Escort.objects.filter(membership_id__exact=10)
	VIP_list = list(VIP_Escorts)
	shuffle(VIP_list)
	return render(request, 'VIP.html', {'VIP_list': VIP_list})


def PremiumEscortsView(request):
	Premium_Escorts = Escort.objects.filter(membership_id__exact=9)
	Premium_list = list(Premium_Escorts)
	shuffle(Premium_list)
	return render(request, 'Premium.html', {'Premium_list': Premium_list})


def NewEscortsView(request):
	New_Escorts = Escort.objects.filter(membership_id__exact=8)
	New_list = list(New_Escorts)
	shuffle(New_list)
	return render(request, 'New.html', {'New_list': New_list})
