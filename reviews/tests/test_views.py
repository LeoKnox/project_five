import json
from unittest import mock
from django.test import TestCase
from bookr.reviews.models import Book, Contributor, Review

class JSSetLikeViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(JSSetLIkeViewTest, cls).setUpClass()
        cls.book = Book.objects.create(
            title="Book",
            isbn = "abc1",
            publisher = 1,
        )
        cls.contributor = Contributor.objects.get_for_model(Book)
        cls.review = Review.objects.create(
            content="ddd",
            rating=9,
        )