import django.contrib.auth.urls
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Your Project", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path("admin/", admin.site.urls),
    path("account/", include("users.urls")),
    path("", include("blog.urls")),
    path("api/", include("api.urls")),
    path("docs/", include_docs_urls(title="Bloggy API documentation")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
