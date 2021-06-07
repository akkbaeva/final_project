from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company_image',
                              null=True)
    description = models.TextField()


TURKISH = 'TURKISH'
KYRGYZ = 'KYRGYZ'
JAPANESE = 'JAPANESE'
FAST_FOOD = 'FAST_FOOD'
KOREAN = 'KOREAN'
EUROPEAN = 'EUROPEAN'
VEGETARIAN = 'VEGETARIAN'
OTHER = 'OTHER'
DISH_CATEGORY = (
    (TURKISH, 'TURKISH'),
    (KYRGYZ, 'KYRGYZ'),
    (JAPANESE, 'JAPANESE'),
    (FAST_FOOD, 'FAST_FOOD'),
    (KOREAN, 'KOREAN'),
    (EUROPEAN, 'EUROPEAN'),
    (VEGETARIAN, 'VEGETARIAN'),
    (OTHER, 'OTHER')
)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dish_image',
                              null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                null=True, blank=True)
    category = models.CharField(max_length=100,
                                choices=DISH_CATEGORY,
                                null=True)
    component = models.TextField()
