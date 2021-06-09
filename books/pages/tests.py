from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomeView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)


    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')


    def test_home_contains_correct_html(self):
        self.assertContains(self.response, 'Bookstore Home')


    def test_home_url_resolves_homeview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomeView.as_view().__name__
        )