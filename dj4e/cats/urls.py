from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='cats'
urlpatterns = [
    path('', views.CatView.as_view(), name='all_cats'),
    path('create/', views.CatCreate.as_view(), name='cat_create'),
    path('<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('breeds/', views.BreedView.as_view(), name='breed_list'),
    path('breeds/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breeds/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('breeds/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
