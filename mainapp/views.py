from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.serializers import UserRegistrationSerializer, PostSerializer, CommentSerializer, PostDetailSerializer, CommentPostSerializer

from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from mainapp.models import Post
from mainapp.models import Comment
User = get_user_model()

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action

class UserRegistrationView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:
            return Response({
            'error':'user with such username is already exists'
            }, status=400
            )
        else:
            user = User.objects.create(
                username=username,
                email=email

            )
            user.set_password(password)
            user.save()
            return Response({'message':'Success'}, status=201)
        

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly, )
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter )
    search_fields = (
        'title', 'user__username',
    )
    filterset_fields = (
        'is_draft',
    )
    ordering_fields = (
        'created_at',
    )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        elif self.action == 'add_comment':
            return CommentPostSerializer
        else: return PostDetailSerializer
    
    @action(methods=['get', 'post',], detail=True)
    def add_comment(self, request, *agrs, **kwargss):
        post = self.get_object()
        user = self.request.user
        serializer = CommentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')

        comment = Comment.objects.create(
            post=post,
            user=user,
            text=text
        )
        serializer = CommentPostSerializer(instance=comment).data
        return Response(
            serializer, status=201
        )


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PostUserView(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
    


    # def list(self, request, *args, **kwargs): #get list
    #     return super().list(request, *args, **kwargs)
    
    # def retrieve(self, request, *args, **kwargs): #get retriev
    #     return super().retrieve(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs): #post
    #     return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs): #put
    #     return super().update(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs): #patch
    #     return super().partial_update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs): #delete
    #     return super().destroy(request, *args, **kwargs)
