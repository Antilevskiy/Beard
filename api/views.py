from .models import User, Todo, Post, Album, Comment, Photo
from rest_framework import viewsets
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, TodoSerializer, PostSerializer, AlbumSerializer, CommentSerializer, PhotoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# FROM https://github.com/alanjds/drf-nested-routers
class TodoViewSet(viewsets.ViewSet):
    serializer_class = TodoSerializer

    def list(self, request, user_pk):
        queryset = Todo.objects.filter(user_id=user_pk)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(client)
        return Response(serializer.data)


class TodoViewSetDefault(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request, user_pk):
        queryset = Post.objects.filter(user_id=user_pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(client)
        return Response(serializer.data)


class PostViewSetDefault(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AlbumViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request, user_pk):
        queryset = Album.objects.filter(user_id=user_pk)
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Album.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = AlbumSerializer(client)
        return Response(serializer.data)


class AlbumViewSetDefault(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CommentViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request, post_pk):
        queryset = Comment.objects.filter(post_id=post_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(client)
        return Response(serializer.data)


class CommentViewSetDefault(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PhotoViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request, album_pk):
        queryset = Photo.objects.filter(album_id=album_pk)
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Photo.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = PhotoSerializer(client)
        return Response(serializer.data)


class PhotoViewSetDefault(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


def default_view(request):
    return HttpResponse('<h1>Go to:</br><a href=https://stormy-refuge-83490.herokuapp.com/api/v1>api</a>')
