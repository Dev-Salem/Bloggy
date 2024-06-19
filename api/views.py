from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets

from blog.models import Blog

from .custom_permissions import isAuthorOrReadOnly
from .serializers import BlogSerializer, UserSerializer

# class BlogListAPIView(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (isAuthorOrReadOnly,)
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
