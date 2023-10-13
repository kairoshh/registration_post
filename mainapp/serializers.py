from rest_framework import serializers
from mainapp.models import Post
from mainapp.models import Comment
class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = (
            'id', 'text',
            'created_at',
            'user','post',
            'username',

        )
        read_only_fields = (
            'user',
        )

class PostSerializer(serializers.ModelSerializer): 
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = (
            'id', 'title',
            'created_at',
            'image',
            'username', 
        )
        read_only_fields = (
            'user',
        )
class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = (
            'id', 'title',
            'created_at', 'image',
            'description', 'user', 
            'username', 'is_draft',
            "comments",
        )

        read_only_fields = (
            'user',
        )

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'created_at', 'text', 'user',
        )
        read_only_fields = (
            'user',
         
         )
        