from django.test import SimpleTestCase
from django.urls import reverse, resolve

from polls.views import HomeView, CategoryView, VoteView, ResultView, ModalView

class TestUrls(SimpleTestCase):

    def test_resolve_home_url(self):
        url = reverse('polls:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_resolve_category_url(self):
        url = reverse('polls:category', kwargs={'category': 'president'})
        self.assertEquals(resolve(url).func.view_class, CategoryView)

    def test_resolve_vote_url(self):
        url = reverse('polls:vote', kwargs={'pk': '1'})
        self.assertEquals(resolve(url).func.view_class, VoteView)

    def test_resolve_result_url(self):
        url = reverse('polls:result', kwargs={'category': 'president'})
        self.assertEquals(resolve(url).func.view_class, ResultView)

    def test_resolve_modal_url(self):
        url = reverse('polls:modal_view', kwargs={'pk': '1'})
        self.assertEquals(resolve(url).func.view_class, ModalView)
