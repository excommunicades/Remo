from django.urls import path
from .views import (
    UserProfileDetailView,
    UserProfilePublicView,
    update_profile,)

urlpatterns = [
    path('', UserProfileDetailView.as_view(), name='profile_detail'),
    path('<str:username>', UserProfilePublicView.as_view(), name='profile_public'),
    path('update/', update_profile, name='update_profile'),
]
