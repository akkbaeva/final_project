from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from food_user import views

router = DefaultRouter()
router.register('', views.UserFilterSearch, basename='user-filter')

urlpatterns = [
    path('api/v1/register/', views.RegisterView.as_view()),
    path('api/v1/carriage/', views.CarriageAPIView.as_view()),
    path('api/v1/search-user/', include(router.urls)),
    path('api/v1/login/', views.FoodObtainTokenPairView.as_view()),
    path('api/v2/login/', TokenObtainPairView.as_view()),
    path('api/v1/login/refresh/', TokenRefreshView.as_view()),
    path('api/v1/login/verify/', TokenVerifyView.as_view()),

]
