from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# The class is used for solving problem with now working LOGOUT_REDIRECT_URL parameter in 'django.contrib.auth'.
# The class redirects user to the `home.html` template
class SignedOutView(TemplateView):
    template_name = 'home.html'

    def get(self, request: HttpRequest, **kwargs):
        logout(request)
        return render(request, self.template_name)
