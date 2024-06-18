from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Blog, Comment


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("blogs")
    login_url = "login"

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogCreateView(
    LoginRequiredMixin,
    CreateView,
):
    model = Blog
    template_name = "blog/create_blog.html"
    fields = ("title", "body")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(
    LoginRequiredMixin,
    UpdateView,
):
    model = Blog
    fields = ("title", "body")
    template_name = "blog/create_blog.html"
    login_url = "login"

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/single_blog.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = "body"
    template_name = "blog/single_blog.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
