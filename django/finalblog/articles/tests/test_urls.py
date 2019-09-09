from django.test import SimpleTestCase
from django.urls import reverse, resolve
from articles.views import post_new, add_comment_to_post, article_detail, article_each, PostUpdateView
from accounts.views import signup_view, logout_view, profile
from finalblog.views import homepage, about, contact


class TestUrls(SimpleTestCase):

    def test_create_is_resolved(self):
        url = reverse('articles:create')
        print(resolve(url))
        self.assertEquals(resolve(url).func, post_new)

    def test_comment_is_resolved(self):
        url = reverse('articles:add_comment_to_post', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_comment_to_post)

    def test_detail_is_resolved(self):
        url = reverse('articles:detail', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, article_detail)

    def test_each_is_resolved(self):
        url = reverse('articles:each', kwargs={'types': 'c'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, article_each)

    def test_update_is_resolved(self):
        url = reverse('articles:update', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, PostUpdateView)

    def test_signup_is_resolved(self):
        url = reverse('accounts:signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup_view)

    def test_signin_is_resolved(self):
        url = reverse('accounts:profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_signout_is_resolved(self):
        url = reverse('accounts:logout')
        try:
            print(resolve(url))
        except AssertionError:
            self.assertEquals(resolve(url).func, logout_view)

    def test_homepage_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage)

    def test_about_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_contact_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)
