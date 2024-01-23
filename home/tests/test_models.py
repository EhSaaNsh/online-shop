from django.test import TestCase
from home.models import Category
from model_bakery import baker


class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = baker.make(Category, name='laptop')

    def test_str_product(self):
        self.assertEqual(str(self.category), 'laptop')
