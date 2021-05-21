from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
