from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import CustomUserCreationForm
# Create your views here.
class SignedOutView(TemplateView):
    template_name = 'home.html'

    def get(self, request: HttpRequest, **kwargs):
        logout(request)
        return render(request, self.template_name)


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
