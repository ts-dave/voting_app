from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUser
from polls.models import Candidate, Category


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        CustomUser.objects.create_user(username='john', password='johnpassword')
        cat = Category(category_name="President")
        cat.save()
        Candidate.objects.create(category=cat, name="Tsatsu", image="images\1.jpg", num_of_votes=0)

        return super().setUp()

    def test_login(self):
        url = reverse("accounts:login")
        response = self.client.post(url, {"username": "john", "password": "johnpassword"})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomUser.objects.first().username, 'john')
        self.assertEquals(CustomUser.objects.count(), 1)
        self.assertTemplateUsed("login.html")
        self.assertRedirects(response, reverse("polls:home"))

    def test_not_logged_in(self):
        url = reverse("accounts:login")
        response = self.client.post(url, {"username": "john", "password": "johnpassw"})
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed("login.html")
        self.assertRedirects(response, reverse("accounts:login"))

    def test_home_view_GET_with_login(self):
        self.client.post(reverse("accounts:login"), {"username": "john", "password": "johnpassword"})
        response = self.client.get(reverse('polls:home'))
        self.assertEquals(response.status_code, 200)

    def test_category_view_GET(self):
        self.client.post(reverse("accounts:login"), {"username": "john", "password": "johnpassword"})
        response = self.client.get(reverse("polls:category", kwargs={'category': 'President'}))
        self.assertEquals(Candidate.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("vote.html")

# TODO: Test Voteview, ResultView and ModalView
