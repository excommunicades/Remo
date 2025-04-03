from django.urls import path
from .views import UserProfileDetailView, UserProfilePublicView

urlpatterns = [
    path('', UserProfileDetailView.as_view(), name='profile_detail'),
    path('<str:username>', UserProfilePublicView.as_view(), name='profile_public'),
]
