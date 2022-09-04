from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitlesViewSet, TokenCreateViewSet,
                    UserSignUpViewSet, UserViewSet)

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)

v1_router.register('users', UserViewSet, basename='users')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('titles', TitlesViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', UserSignUpViewSet.as_view()),
    path('v1/auth/token/', TokenCreateViewSet.as_view()),
]
