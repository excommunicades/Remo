from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError

def login_or_register(request):
    if request.method == 'POST':
        print(request.method)
        if 'login_username' in request.POST:

            username = request.POST.get('login_username')
            password = request.POST.get('login_password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'redirect': '/restaurants/main'})
            else:
                return JsonResponse({'status': 'error', 'error': 'Invalid username or password.'})


        elif 'registration_username' in request.POST:

            username = request.POST.get('registration_username')
            email = request.POST.get('registration_email')
            password = request.POST.get('registration_password')
            confirm_password = request.POST.get('registration_confirm_password')

            print(username, email, password, confirm_password)

            if password != confirm_password:
                return JsonResponse({'status': 'error', 'errors': {'registration_confirm_password': 'Passwords do not match'}})

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                return JsonResponse({'status': 'success', 'redirect': '/restaurants/main'})
            except ValidationError as e:
                return JsonResponse({'status': 'error', 'errors': {'registration_email': str(e)}})

    return render(request, 'authy/Authorization.html')
