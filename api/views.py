from .models import User, Todo, Post, Album, Comment, Photo
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, TodoSerializer, PostSerializer, AlbumSerializer, CommentSerializer, PhotoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# CLASSIC
'''
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
'''

# 2nd try FROM https://medium.com/swlh/using-nested-routers-drf-nested-routers-in-django-rest-framework-951007d55cdc
'''
class TodoViewSet(viewsets.ModelViewSet):
    """Todo Viewset"""
    queryset = Todo.objects.all().select_related(
        'user'
    )
    serializer_class = TodoSerializer

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get("user_pk")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise 'A library with this id does not exist'
        return self.queryset.filter(user=user)
'''


# FROM https://github.com/alanjds/drf-nested-routers
class TodoViewSet(viewsets.ViewSet):
    serializer_class = TodoSerializer

    def list(self, request,):
        queryset = Todo.objects.filter()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(client)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
