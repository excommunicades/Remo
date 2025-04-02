from django.urls import path

from authy.views import login_or_register
urlpatterns = [
    path('', login_or_register, name='auth_view'),
]
