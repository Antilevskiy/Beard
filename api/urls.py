from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path, include
from .views import UserViewSet, TodoViewSet, PostViewSet, AlbumViewSet, CommentViewSet, PhotoViewSet
from .views import TodoViewSetDefault, PostViewSetDefault, AlbumViewSetDefault, CommentViewSetDefault, PhotoViewSetDefault


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'todos', TodoViewSetDefault, basename="todo")
router.register(r'posts', PostViewSetDefault, basename="post")
router.register(r'albums', AlbumViewSetDefault, basename="album")
router.register(r'comments', CommentViewSetDefault, basename="comment")
router.register(r'photos', PhotoViewSetDefault, basename="photo")

todo_router = routers.NestedSimpleRouter(
    router,
    r'users',
    lookup='user')
todo_router.register(
    r'todos',
    TodoViewSet,
    basename='user-todo'
)

post_router = routers.NestedSimpleRouter(
    router,
    r'users',
    lookup='user')
post_router.register(
    r'posts',
    PostViewSet,
    basename='user-post'
)

album_router = routers.NestedSimpleRouter(
    router,
    r'users',
    lookup='user')
album_router.register(
    r'albums',
    AlbumViewSet,
    basename='user-album'
)

comment_router = routers.NestedSimpleRouter(
    router,
    r'posts',
    lookup='post')
comment_router.register(
    r'comments',
    CommentViewSet,
    basename='post-comment'
)

photo_router = routers.NestedSimpleRouter(
    router,
    r'albums',
    lookup='album')
photo_router.register(
    r'photos',
    PhotoViewSet,
    basename='album-photo'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(todo_router.urls)),
    path('', include(post_router.urls)),
    path('', include(album_router.urls)),
    path('', include(comment_router.urls)),
    path('', include(photo_router.urls))
]
