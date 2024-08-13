from django.urls import path
from .endpoints import (
    PostsPublicListAPIView,
    PostsPrivateListAPIView,
    PostCreateAPIView,
    PostRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('posts/public/', PostsPublicListAPIView.as_view(), name='public-posts'),
    path('posts/private/', PostsPrivateListAPIView.as_view(), name='private-posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name='create-post'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieveupdatedestroy'),
]