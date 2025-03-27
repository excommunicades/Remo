from django.urls import path

from authy.views import Authorization
urlpatterns = [
    path('login', Authorization, name='login_user'),
]
