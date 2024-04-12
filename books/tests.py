import os
import uuid

from accounts.models import CustomUser
from django.db.models.functions import datetime
from django.test import TestCase
from django.urls import reverse

from djangoBookStore.settings import MEDIA_ROOT
from .models import Book, Review
from django.core.files.uploadedfile import SimpleUploadedFile


class BookTests(TestCase):
    user = None
    book = None

    @classmethod
    def setUpTestData(cls):
        folder_name = MEDIA_ROOT / 'images'
        file_path = os.path.join(folder_name, 'test_image.jpg')
        cover_file = SimpleUploadedFile(name='test_image.jpg', content=open(file_path, 'rb').read(),
                                        content_type='image/jpeg')

        cls.user = CustomUser.objects.create_user(username='review_test_user', password='review_password123',
                                                  email='review_test_email.gmail.com')
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            publisher="Publisher",
            description="Description",
            price=504,
            cover=cover_file,
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            text="An excellent review",
            date=datetime.datetime.now()
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.publisher}", "Publisher")
        self.assertEqual(f"{self.book.description}", "Description")
        self.assertEqual(f"{self.book.price}", "504")
        # Assert cover file
        expected_cover_path = os.path.join(MEDIA_ROOT, str(self.book.cover))
        with open(expected_cover_path, 'rb') as expected_cover:
            expected_content = expected_cover.read()
            actual_content = self.book.cover.read()
            self.assertEqual(expected_content, actual_content, "Cover file content doesn't match")

    def test_book_list_view(self):
        response = self.client.get(reverse("all_book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "504")
        self.assertTemplateUsed(response, "book/all_book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/book/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "Publisher")
        self.assertContains(response, "Description")
        self.assertContains(response, "JK Rowling")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "book/book_detail.html")
