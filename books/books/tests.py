from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Book, Review


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        self.review = Review.objects.create(
            book = self.book,
            author = self.user,
            review = 'An excellent review'
        )


    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')


    def test_book_list_view_for_logged_in_users(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('books:list'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Harry Potter')

        self.assertTemplateUsed('books/list.html')


    def test_book_list_view_for_logged_out_users(self):
        response = self.client.get(reverse('books:list'))

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, f"{reverse('account_login')}?next=/books/")
        response = self.client.get(f"{reverse('account_login')}?next=/books/")

        self.assertContains(response, 'Log in')


    def test_book_detail_view_with_permissions(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)

        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/123/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')

        self.assertTemplateUsed(response, 'books/detail.html')