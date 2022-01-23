from django.urls import include, path
<<<<<<< HEAD

from .views import FollowListView, FollowView

urlpatterns = [
    path('users/<int:id>/subscribe/', FollowView.as_view(), name='subscribe'),
    path('users/subscriptions/', FollowListView.as_view(),
         name='subscription'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
=======
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
]