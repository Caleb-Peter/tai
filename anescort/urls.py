from django.urls import path
from . import views

from .views import EscortDetailView, PremiumEscortsView, NewEscortsView, VIPEscortsView, AddEscortView, EditEscortView, DeleteEscortView, LocationView #HomeView

urlpatterns = [
    path('', views.all_escorts, name="home"),
    #path('', HomeView.as_view(), name="home"),
    path('escort/<int:pk>', EscortDetailView.as_view(), name="escort-details"),
    path('postad/', AddEscortView.as_view(), name="add-escort"),
    path('escort/update/<int:pk>', EditEscortView.as_view(), name="update-escort"),
    path('escort/<int:pk>/remove', DeleteEscortView.as_view(), name="delete-escort"),
    path('location/<str:locs>/', LocationView, name='location'),
    path('membership/vip/', views.VIPEscortsView, name='vip-members'),
    path('membership/premium/', views.PremiumEscortsView, name='premium-members'),
    path('membership/new/', views.NewEscortsView, name='new-members'),
    
]
