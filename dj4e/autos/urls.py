from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('makes/', views.MakeView.as_view(), name='makes'),
]
