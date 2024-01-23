from django.test import TestCase
from home.views import HomeView, ProductDetailView, BucketHomeView, DeleteObjectBucketView
from django.urls import resolve, reverse


class TestUrls(TestCase):
    def test_get_home_url(self):
        url = reverse('home:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_category_filter(self):
        url = reverse('home:category_filter', args=('apple-laptop',))
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_product_detail(self):
        url = reverse('home:product_detail', args=('dell-laptop', ))
        self.assertEqual(resolve(url).func.view_class, ProductDetailView)

    def test_bucket_home(self):
        url = reverse('home:bucket')
        self.assertEqual(resolve(url).func.view_class, BucketHomeView)

    def test_delete_object_bucket_view(self):
        url = reverse('home:delete_obj_bucket', args=('1', ))
        self.assertEqual(resolve(url).func.view_class, DeleteObjectBucketView)






