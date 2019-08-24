from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdsListView.as_view(), name='ads' ),
    path('<int:pk>/', views.AdsDetailView.as_view(), name='ad_detail'),
    path('create/', views.AdsCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view(), name='ad_delete')
]
