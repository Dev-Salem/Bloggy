from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blogs"),
    path("create-blog/", views.BlogCreateView.as_view(), name="create-blog"),
    path("delete-blog/<int:pk>/", views.BlogDeleteView.as_view(), name="delete-blog"),
    path("update-blog/<int:pk>/", views.BlogUpdateView.as_view(), name="update-blog"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog"),
    path("create-blog/", views.CommentCreateView.as_view(), name="create-blog"),
]
