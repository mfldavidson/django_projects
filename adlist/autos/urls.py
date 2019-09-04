from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('', views.AutosListView.as_view(), name='all_autos' ),
    path('auto/<int:pk>/', views.AutosDetailView.as_view(), name='auto_detail'),
    path('create/', views.AutosCreateView.as_view(), name='auto_create'),
    path('auto/<int:pk>/update/', views.AutosUpdateView.as_view(), name='auto_update'),
    path('auto/<int:pk>/delete/', views.AutosDeleteView.as_view(), name='auto_delete'),
    path('auto/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('auto_list')), name='comment_delete'),
]
