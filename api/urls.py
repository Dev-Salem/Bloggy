from django.urls import include, path

from .views import BlogDetailAPIView, BlogListAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog-list"),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("<int:pk>/", BlogDetailAPIView.as_view(), name="blog-detail"),
    path("accounts/", include("allauth.urls")),
]
