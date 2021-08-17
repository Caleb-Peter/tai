from django.urls import path
#from . import views
from .views import BlogView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('addpost/', AddPostView.as_view(), name="add_post"),
    path('updatepost/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('deletepost/<int:pk>', DeletePostView.as_view(), name="delete_post"),


]