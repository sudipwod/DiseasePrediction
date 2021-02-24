from django.test import TestCase, client
from django.urls import reverse
from main_app.models import patient, doctor, Hospital, diseaseinfo, consultation
import json

class TestViews(TestCase):
    def setUP(self):
        client = Client()
        self.list_url = reverse('checkdisease')
    
    
    def test_checkdisease_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient/checkdisease/checkdisease.html')
