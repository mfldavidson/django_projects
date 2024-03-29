from django.urls import path, reverse_lazy
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.AdsListView.as_view(), name='all_ads' ),
    path('ad/<int:pk>/', views.AdsDetailView.as_view(), name='ad_detail'),
    path('create/', views.AdsCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update', views.AdsUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('ad_list')), name='comment_delete'),
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
