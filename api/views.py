from rest_framework import generics, permissions

from blog.models import Blog

from .custom_permissions import isAuthorOrReadOnly
from .serializers import BlogSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
