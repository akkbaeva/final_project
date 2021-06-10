# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from food_user.models import FoodUser, Carriage
from food_user.serializers import RegisterSerializer, CarriageSerializer, UserSerializer, FoodObtainPairSerializer


class FoodObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = FoodObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = FoodUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class CarriageAPIView(generics.ListCreateAPIView,
                      mixins.DestroyModelMixin):
    serializer_class = CarriageSerializer
    queryset = Carriage.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request)


class UserFilterSearch(viewsets.ModelViewSet):
    queryset = FoodUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['username', 'number']
    search_fields = ['=username', '=number']
