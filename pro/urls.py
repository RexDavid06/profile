from django.urls import path

from . import views


urlpatterns = [
    path('me/', views.profileView.as_view(), name='profile'),
]