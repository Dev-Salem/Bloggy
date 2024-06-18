from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "users/home.html"

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blogs')
    template_name = 'users/register.html'