from rest_framework.routers import DefaultRouter

from apps.tweets.views import TweetViewSet

app_name = 'tweets'

router = DefaultRouter()
router.register('', TweetViewSet)

urlpatterns = list()
urlpatterns += router.urls
