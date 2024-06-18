import django.contrib.auth.urls as auth
from django.urls import include, path

from .views import *

urlpatterns = [
    path("account/", include("django.contrib.auth.urls")),
    path("", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
]
# templates / registration
