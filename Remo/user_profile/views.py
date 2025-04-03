from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError


def main(request):
    return render(request, 'restaurants/Main.html')