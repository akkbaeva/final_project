from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.
from category_food.models import Dish

ADMIN = 'ADMIN'
CLIENT = 'CLIENT'
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (CLIENT, 'CLIENT')
)


class FoodUser(AbstractBaseUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    user_type = models.CharField(max_length=100, choices=USER_TYPE)
    username = models.CharField('username',
                                max_length=100,
                                unique=True)
    first_name = models.CharField('first_name',
                                  max_length=100, null=True, blank=True)
    last_name = models.CharField('last_name',
                                 max_length=100, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['number']


class Carriage(models.Model):
    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'
    user = models.ForeignKey(FoodUser, on_delete=models.CASCADE,
                             null=True, related_name='carriage_user')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,
                             null=True, related_name='user_choice_dish')
