from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(description="Retrieve a list of public posts"),
)
class PostsPublicListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

@extend_schema_view(
    get=extend_schema(description="Retrieve a list of private posts for subscribers"),
)
class PostsPrivateListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'subscriber':
            return Post.objects.filter(is_public=False)
        return Post.objects.none()

@extend_schema_view(
    post=extend_schema(description="Create a new post (only for authors)"),
)
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'author':
            raise PermissionDenied('Only authors can create articles.')
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Post created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

@extend_schema_view(
    get=extend_schema(description="Retrieve a post by its ID"),
    put=extend_schema(description="Update a post (only by the author)"),
    delete=extend_schema(description="Delete a post (only by the author)"),
)
class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit this article.')
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Post updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('You do not have permission to delete this article.')
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Post deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)