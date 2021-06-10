from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from category_food.serializers import DishSerializer
from food_user.models import FoodUser, Carriage


class FoodObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(FoodObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=FoodUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = FoodUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'number',
                  'password',
                  'password2',)
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields did not match.'})

        return attrs

    def create(self, validated_data):
        user = FoodUser.objects.create(
            username=validated_data['username'],
            number=validated_data['number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodUser
        fields = ('username', 'number')


class CarriageSerializer(serializers.ModelSerializer):
    user = UserSerializer
    dish = DishSerializer

    class Meta:
        model = Carriage
        fields = ('user', 'dish')
