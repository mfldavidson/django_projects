from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='autos'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.AutoCreate.as_view(), name='auto_create'),
    path('int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('makes/', views.MakeView.as_view(), name='make_list'),
    path('makes/create/', views.MakeCreate.as_view(), name='make_create'),
    path('makes/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('makes/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]
