from django.urls import path

from food_user import views

urlpatterns = [
    path('api/v1/register/', views.RegisterView.as_view()),
]