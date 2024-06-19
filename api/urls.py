from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import BlogViewSet, UserViewSet

router = SimpleRouter()
router.register("accounts", UserViewSet, basename="accounts")
router.register("", BlogViewSet, basename="api-blogs")
urlpatterns = router.urls
print(urlpatterns)
# urlpatterns = [
#     path("", BlogListAPIView.as_view(), name="blog-list"),

#     path("accounts/", include("allauth.urls")),
# ]
