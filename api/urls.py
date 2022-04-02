from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path, include
from .views import UserViewSet, TodoViewSet, PostViewSet, AlbumViewSet, CommentViewSet, PhotoViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
#router.register(r'users/(?P<user_id>\d+)/todos', TodoViewSet, basename='user-todo')
#router.register(r'users/(?P<user_id>\d+)/posts', PostViewSet, basename='user-post')
router.register(r'todos', TodoViewSet, basename="todo")
router.register(r'posts', PostViewSet, basename="post")
router.register(r'albums', AlbumViewSet, basename="album")
router.register(r'comments', CommentViewSet, basename="comment")
router.register(r'photos', PhotoViewSet, basename="photo")

todo_router = routers.NestedSimpleRouter(
    router,
    r'users',
    lookup='user')
todo_router.register(
    r'todos',
    TodoViewSet,
    basename='user-todo'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(todo_router.urls)),
]
