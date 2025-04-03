from django.http import JsonResponse

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from user_profile.models import UserProfile

def registration_logic_function(request, username, email, password, confirm_password):

    ''' Validate data, create user, return response to server. '''

    status, error_response = validate_user_registration(
                        request.POST['registration_username'],
                        request.POST['registration_email'],
                        request.POST['registration_password'],
                        request.POST['registration_confirm_password'])

    if status:
        return error_response   

    return create_user(username, email, password)

def create_user(username, email, password):

    ''' Create user by args. '''

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)
        return JsonResponse({'status': 'success', 'redirect': '/restaurants/main'})
    except ValidationError as e:
        return JsonResponse({'status': 'error', 'type': 'registration', 'error_field': 'Form', 'error': 'Error.'})


def validate_user_registration(username, email, password, confirm_password):

    ''' Validate user by username/email unique check. Passwords on matching. '''

    if check_user_by_username(username):
        return True, JsonResponse({'status': 'error', 'type': 'registration', 'error_field': 'Username', 'error': 'User with this username already exist.'})
    if check_user_by_email(email):
        return True, JsonResponse({'status': 'error', 'type': 'registration', 'error_field': 'Email', 'error': 'User with this email already exist.'})

    if password != confirm_password:
        return True, JsonResponse({'status': 'error', 'type': 'registration', 'error_field': 'Confirm_Password', 'error': 'Confirm password mush match to password.'})

    return False, None


def check_user_by_username(username) -> bool:

    ''' Check does db has user by username. '''

    return User.objects.filter(username=username).exists()

def check_user_by_email(email) -> bool:

    ''' Check does db has user by username. '''

    return User.objects.filter(email=email).exists()
