from django.urls import path

from .views import BlogDetailAPIView, BlogListAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog-list"),
    path("<int:pk>/", BlogDetailAPIView.as_view(), name="blog-detail"),
]
