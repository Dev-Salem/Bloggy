from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import ModelFormMixin

from .forms import CommentForm
from .models import Blog, Comment


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    paginate_by = 3

    def get_queryset(self):
        try:
            query = self.request.GET["q"]
        except:
            query = ""
        object_list = super().get_queryset()
        object_list = Blog.objects.filter(title__icontains=query)
        return object_list


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


class BlogDetailView(ModelFormMixin, DetailView):
    model = Blog
    template_name = "blog/single_blog.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog", kwargs={"pk": self.get_object().id})

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            form.instance.blog = self.get_object()
        else:
            raise PermissionDenied
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = None
        return kwargs

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = "body"
    template_name = "blog/single_blog.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
