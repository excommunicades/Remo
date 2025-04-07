from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .utils import (
    check_user_by_username,
    registration_logic_function,
)

def login_or_register(request):

    ''' Login or register user in dependency of request type '''

    if request.method == 'POST':
        if 'login_username' in request.POST:

            username = request.POST.get('login_username')
            password = request.POST.get('login_password')

            if not check_user_by_username(username):
                return JsonResponse({'status': 'error', 'type': 'login', 'error_field': 'Username', 'error': 'User does not exist.'})

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'redirect': '/profile'})
            else:
                return JsonResponse({'status': 'error', 'type': 'login', 'error_field': 'Password', 'error': 'Wrong Password.'})


        elif 'registration_username' in request.POST:

            return registration_logic_function(
                                request,
                                request.POST.get('registration_username'),
                                request.POST.get('registration_email'),
                                request.POST.get('registration_password'),
                                request.POST.get('registration_confirm_password'))

    return render(request, 'authy/Authorization.html')
