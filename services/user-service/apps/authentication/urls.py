from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('refresh-token/', views.refreshToken, name='refresh-token'),
]
