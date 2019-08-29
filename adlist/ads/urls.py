from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('', views.AdsListView.as_view(), name='ads' ),
    path('<int:pk>/', views.AdsDetailView.as_view(), name='ad_detail'),
    path('create/', views.AdsCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update',
        views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')), name='comment_delete'),
]
