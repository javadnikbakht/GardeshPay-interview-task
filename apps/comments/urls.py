from rest_framework.routers import DefaultRouter

from apps.comments.views import CommentViewSet

app_name = 'comments'

router = DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = list()
urlpatterns += router.urls
