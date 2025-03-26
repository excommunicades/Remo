from django.urls import path

from restaurants.views import generate_html_template
urlpatterns = [
    path('main', generate_html_template, name='generate_html')
]
