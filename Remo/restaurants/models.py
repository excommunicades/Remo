from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurants(models.Model):

    '''Restaurant model'''

    name = models.CharField(max_length=50, blank=False, db_index=True)
    cuisine_type = models.CharField(max_length=30, blank=False, db_index=True)
    description = models.TextField(blank=True)
    latitude = models.FloatField(blank=True) # blank=False
    longitude = models.FloatField(blank=True) # blank=False
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Restaurants' 

class Restaurants_Reviews(models.Model):

    '''Reviews model for restaurant object'''

    restaurant = models.ForeignKey(Restaurants, blank=False, related_name='restaurant_reviews', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, blank=False, related_name='user_reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    rating = models.FloatField(
                            default=0.0,
                            validators=[
                                MinValueValidator(0.0),
                                MaxValueValidator(5.0),
                                ]
                          )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Restaurants_Reviews'
