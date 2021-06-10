from django.urls import path

from singer_album import views

urlpatterns = [
    path('api/v1/singer/', views.SingerAPIView.as_view()),
    path('api/v1/album/', views.AlbumAPIView.as_view()),
]