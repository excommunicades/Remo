import traceback

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import UserProfile

class UserProfileDetailView(DetailView):

    model = UserProfile
    template_name = 'user_profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)

class UserProfilePublicView(DetailView):

    model = UserProfile
    template_name = 'user_profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):

        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return get_object_or_404(UserProfile, user=user)

@login_required
def update_profile(request):


    if request.method == "POST":
        try:
            print(request.user.id)
            user = UserProfile.objects.get(user=request.user.id)
            location = request.POST.get('location')
            bio = request.POST.get('bio')
            print(location, bio)

            # Если данные получены, обновляем профиль
            if location is not None:
                user.location = location
            if bio is not None:
                user.bio = bio
            
            user.save()
            print(user.location, user.bio)

            return JsonResponse({'status': 'success', 'location': user.location, 'bio': user.bio})

        except Exception as e:

            print("An error:", e)
            traceback.print_exc()

            return JsonResponse({'status': 'error', 'message': 'An error occurred while updating the profile.'}, status=500)

    return render(request, 'user_profile/profile_detail.html')
