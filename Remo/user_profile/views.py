from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'user_profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Получаем профиль текущего пользователя
        return get_object_or_404(UserProfile, user=self.request.user)

class UserProfilePublicView(DetailView):
    model = UserProfile
    template_name = 'user_profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Получаем профиль по имени пользователя (username)
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return get_object_or_404(UserProfile, user=user)
