from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="user", email="user@email.com", password="user123"
        )

        self.assertEqual(user.username, "user")
        self.assertEqual(user.email, "user@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="superadmin123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    # This test verifies that the signup form used in the signup page is an instance of CustomUserCreationForm.
    # It also checks whether the response contains the 'csrfmiddlewaretoken'
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    # This test checks whether the URL '/accounts/signup/' resolves to the expected view function,
    # which is SignupPageView. It uses Django's resolve function to match the URL to its corresponding view function.
    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
