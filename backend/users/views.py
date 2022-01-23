<<<<<<< HEAD
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.pagination import LimitPageNumberPagination

from .models import Subscribe, User
from .serializers import SubscriptionListSerializer, SubscriptionSerializer


class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        data = {'user': request.user.id, 'following': id}
        serializer = SubscriptionSerializer(
            data=data, context={'request': request})
=======
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from foodgram.paginations import CustomPageNumberPaginator
from foodgram.permissions import AuthorOrAdminOrRead
from users.models import Follow, User
from users.serializers import (CustomUserSerializer, FollowGetSerializer,
                               FollowPostSerializer)


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomPageNumberPaginator
    permission_classes = (AuthorOrAdminOrRead, )

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def subscriptions(self, request):
        """Статус подписки."""
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowGetSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    def subscribe(self, request, id=None):
        """Подписка."""
        user = request.user
        author = get_object_or_404(User, id=id)
        data = {
            'user': user.id,
            'author': author.id,
        }
        serializer = FollowPostSerializer(
            data=data, context={'request': request}
        )
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

<<<<<<< HEAD
    def delete(self, request, id):
        user = request.user
        following = get_object_or_404(User, id=id)
        subscribe = get_object_or_404(
            Subscribe, user=user, following=following)
        subscribe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitPageNumberPagination

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(following__user=user)
        page = self.paginate_queryset(queryset)
        serializer = SubscriptionListSerializer(
            page, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
=======
    @subscribe.mapping.delete
    def unsubscribe(self, request, id=None):
        """Отписка."""
        user = request.user
        author = get_object_or_404(User, id=id)
        subscribe = get_object_or_404(
            Follow, user=user, author=author
        )
        subscribe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
