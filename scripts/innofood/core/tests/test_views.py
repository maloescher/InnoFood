from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from core.views import customer_page
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestViews:

    def test_customer_autherntificated(self):
        path = 'cafelist'
        request = RequestFactory().get(path)
        request.user = mixer.blend('core.Customer')

        response = customer_page(request)
        assert response.status_code == 200