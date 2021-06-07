from rest_framework import serializers

from category_food.models import Company, Dish


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id',
                  'name',
                  'image',
                  'description')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id',
                  'name',
                  'image',
                  'category',
                  'component',
                  'company')
