from django.test import RequestFactory
from django.urls import reverse
# from django.contrib.auth.models import User
# from core.views import *
# from mixer.backend.django import mixer
import pytest
from django.test import Client



@pytest.mark.django_db
class TestViews:

    client = Client()

    def test_customer_autherntificated(self):
        path = 'cafes/'
        request = RequestFactory().get(path)
        response = self.client.get(path)
        assert response.status_code == 200