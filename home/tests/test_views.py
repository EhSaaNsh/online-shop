from django.test import TestCase, Client
from home.views import HomeView, BucketHomeView, ProductDetailView
from django.urls import reverse, resolve
from home.models import Category

class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories = Category.objects.create(name='laptop', is_sub=False, slug='laptop')

    def test_get_home_view(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.failUnless(response.context['categories'], self.categories)


# class TestProductDetailView(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_product_detail_view(self):
#         response = self.client.get(reverse('home:product_detail', args=('laptop', )))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home/detail.html')



