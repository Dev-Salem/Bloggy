from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import BlogViewSet, CommentViewSet, UserViewSet

router = SimpleRouter()
router.register("accounts", UserViewSet, basename="accounts")
router.register("comments", CommentViewSet, basename="comments")
router.register("", BlogViewSet, basename="api-blogs")
urlpatterns = router.urls
print(urlpatterns)
