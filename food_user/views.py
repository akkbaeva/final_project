
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from food_user.models import FoodUser
from food_user.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = FoodUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )