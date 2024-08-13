from rest_framework import serializers
from .models import Post

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'is_public',
            'author',
        ]
        read_only_fields = ['author']