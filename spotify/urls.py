from django.urls import path
from . import views

urlpatterns = [
    path('get-auth-url/', views.AuthURL.as_view()),
    path('redirect/', views.spotify_callback),
]
