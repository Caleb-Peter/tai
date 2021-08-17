from django.urls import path
from .views import UserRegisterView, UserEditView

urlpatterns = [
  path('register14653625525hss00988jjh656263636ghannhsshu/', UserRegisterView.as_view(), name='register'),
  path('update-profile/', UserEditView.as_view(), name='update-profile'),


]
