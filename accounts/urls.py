from django.urls import path
from .views import SignupPageView
from accounts.views import SignedOutView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("signed-out/", SignedOutView.as_view(), name="sign-out"),

]
