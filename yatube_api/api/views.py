from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins

from .serializers import CommentSerializer, GroupSerializer
from .serializers import FollowSerializer, PostSerializer
from posts.models import Group, Post, User
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Класс Пост для обработки  запросов:
    GET,POST,DELETE,PATCH"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс Коментарии для обработки комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс Группы только для чтения"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Класс Follow для управлениями подписок пользователя"""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        following = get_object_or_404(
            User,
            username=self.request.user.username
        )

        return following.follower.all()
