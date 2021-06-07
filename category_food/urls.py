from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category_food import views

router = DefaultRouter()
router.register('', views.CompanyAPIView, basename='company_list')
router.register('', views.CompanyAPIView, basename='company_detail')

urlpatterns = [
    path('api/v1/companies/', include(router.urls)),
    path('api/v1/companies/<int:id>/', include(router.urls)),
    path('api/v1/dish/', views.DishAPIView.as_view()),
    path('api/v1/dish/<int:id>/', views.DishDetailAPIView.as_view())
]